#!/usr/bin/env python3
"""Radar do Orçamento — curadoria diária de notícias sobre orçamento público federal.

Pipeline:
  1. Coleta notícias do dia no Google Notícias (RSS gratuito).
  2. Deduplica por link/título.
  3. Usa o Opus 4.8 (via OpenRouter) para escrever uma narrativa-radar.
  4. Envia a narrativa + os links para o Telegram.

Configuração por variáveis de ambiente (GitHub Actions Secrets):
  OPENROUTER_API_KEY   chave do OpenRouter
  TELEGRAM_BOT_TOKEN   token do bot do Telegram (via @BotFather)
  TELEGRAM_CHAT_ID     id do chat de destino (seu usuário)
  OPENROUTER_MODEL     (opcional) slug do modelo; padrão: anthropic/claude-opus-4.8
"""

from __future__ import annotations

import html
import os
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta

import requests

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "anthropic/claude-opus-4.8")

# Termos de busca no Google Notícias. Cada um vira um feed RSS.
TERMOS_BUSCA = [
    "orçamento público federal",
    "orçamento da União",
    "PLOA",
    "Lei Orçamentária Anual",
    "Tesouro Nacional orçamento",
    "orçamento Congresso federal",
]

MAX_NOTICIAS = 20  # teto de itens enviados ao LLM
FUSO_BR = timezone(timedelta(hours=-3))  # horário de Brasília
LIMITE_TELEGRAM = 4096  # caracteres por mensagem


# ---------------------------------------------------------------------------
# 1. Coleta
# ---------------------------------------------------------------------------

def url_rss_google_news(termo: str) -> str:
    """Monta a URL do feed RSS de busca do Google Notícias (pt-BR)."""
    q = urllib.parse.quote(termo)
    return (
        f"https://news.google.com/rss/search?q={q}"
        "&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    )


def coletar_noticias() -> list[dict]:
    """Coleta e deduplica notícias de todos os termos de busca.

    Parseia o RSS do Google Notícias com a biblioteca padrão (sem dependências
    que precisem compilar).
    """
    vistos: set[str] = set()
    noticias: list[dict] = []

    for termo in TERMOS_BUSCA:
        try:
            resp = requests.get(url_rss_google_news(termo), timeout=30)
            resp.raise_for_status()
            raiz = ET.fromstring(resp.content)
        except (requests.RequestException, ET.ParseError) as erro:
            print(f"  aviso: falha ao coletar '{termo}': {erro}")
            continue

        for item in raiz.findall(".//item"):
            titulo = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            if not titulo or not link:
                continue

            chave = titulo.lower()
            if chave in vistos:
                continue
            vistos.add(chave)

            elem_fonte = item.find("source")
            fonte = (elem_fonte.text or "").strip() if elem_fonte is not None else ""

            noticias.append(
                {
                    "titulo": titulo,
                    "link": link,
                    "fonte": fonte,
                    "resumo": (item.findtext("description") or "").strip(),
                }
            )

    return noticias[:MAX_NOTICIAS]


# ---------------------------------------------------------------------------
# 2. Narrativa com o LLM (OpenRouter / Opus 4.8)
# ---------------------------------------------------------------------------

def gerar_radar(noticias: list[dict]) -> str:
    """Pede ao Opus 4.8 (via OpenRouter) uma narrativa-radar das notícias."""
    lista = "\n".join(
        f"{i+1}. {n['titulo']} ({n['fonte'] or 'fonte desconhecida'})"
        for i, n in enumerate(noticias)
    )

    system = (
        "Você é um curador de notícias especializado em orçamento público "
        "federal brasileiro. Escreve um 'radar' diário: claro, direto e "
        "confiável. NUNCA invente fatos — use apenas as manchetes fornecidas. "
        "Se algo não estiver nas manchetes, não afirme."
    )
    user = (
        "Abaixo estão as manchetes do dia sobre orçamento público federal.\n\n"
        f"{lista}\n\n"
        "Escreva uma narrativa-radar em português do Brasil, de 3 a 5 "
        "parágrafos curtos, conectando os temas mais relevantes (decisões, "
        "valores, atores, prazos). Foque no que muda ou no que importa. "
        "Não liste os links — eles serão enviados à parte. Não use títulos "
        "em markdown; escreva em texto corrido."
    )

    resposta = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": OPENROUTER_MODEL,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        },
        timeout=120,
    )
    resposta.raise_for_status()
    dados = resposta.json()
    return dados["choices"][0]["message"]["content"].strip()


# ---------------------------------------------------------------------------
# 3. Envio ao Telegram
# ---------------------------------------------------------------------------

def narrativa_para_html(texto: str) -> str:
    """Converte a marcação leve (markdown) que o LLM possa emitir em HTML do Telegram."""
    t = html.escape(texto)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)  # **negrito**
    t = re.sub(r"__(.+?)__", r"<b>\1</b>", t)        # __negrito__
    t = re.sub(r"(?m)^\s{0,3}#{1,6}\s*(.+)$", r"<b>\1</b>", t)  # # Título
    return t


def montar_mensagem(narrativa: str, noticias: list[dict]) -> str:
    """Monta a mensagem final em HTML para o Telegram."""
    data = datetime.now(FUSO_BR).strftime("%d/%m/%Y")
    partes = [f"<b>📡 Radar do Orçamento — {data}</b>", ""]
    partes.append(narrativa_para_html(narrativa))
    partes.append("")
    partes.append("<b>🔗 Notícias</b>")
    for i, n in enumerate(noticias, 1):
        titulo = html.escape(n["titulo"])
        fonte = f" — {html.escape(n['fonte'])}" if n["fonte"] else ""
        partes.append(f'{i}. <a href="{html.escape(n["link"])}">{titulo}</a>{fonte}')
    return "\n".join(partes)


def fatiar(texto: str, limite: int = LIMITE_TELEGRAM) -> list[str]:
    """Quebra o texto em pedaços que cabem no limite do Telegram (por linha)."""
    pedacos: list[str] = []
    atual = ""
    for linha in texto.split("\n"):
        if len(atual) + len(linha) + 1 > limite:
            pedacos.append(atual)
            atual = ""
        atual += linha + "\n"
    if atual.strip():
        pedacos.append(atual)
    return pedacos


def enviar_telegram(texto: str) -> None:
    """Envia a mensagem ao Telegram, fatiando se passar do limite."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    for pedaco in fatiar(texto):
        resposta = requests.post(
            url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": pedaco,
                "parse_mode": "HTML",
                "disable_web_page_preview": True,
            },
            timeout=30,
        )
        resposta.raise_for_status()


# ---------------------------------------------------------------------------
# Orquestração
# ---------------------------------------------------------------------------

def main() -> int:
    faltando = [
        nome
        for nome, valor in [
            ("OPENROUTER_API_KEY", OPENROUTER_API_KEY),
            ("TELEGRAM_BOT_TOKEN", TELEGRAM_BOT_TOKEN),
            ("TELEGRAM_CHAT_ID", TELEGRAM_CHAT_ID),
        ]
        if not valor
    ]
    if faltando:
        print(f"ERRO: variáveis de ambiente faltando: {', '.join(faltando)}")
        return 1

    print("Coletando notícias…")
    noticias = coletar_noticias()
    print(f"  {len(noticias)} notícias após dedup.")

    if not noticias:
        enviar_telegram(
            "<b>📡 Radar do Orçamento</b>\n\nSem notícias relevantes hoje."
        )
        print("Sem notícias. Enviado aviso ao Telegram.")
        return 0

    print("Gerando narrativa com o LLM…")
    narrativa = gerar_radar(noticias)

    print("Enviando ao Telegram…")
    enviar_telegram(montar_mensagem(narrativa, noticias))
    print("Pronto.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

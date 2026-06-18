# 📡 Curador de Orçamento

Curadoria diária e automática de notícias sobre **orçamento público federal**.
Toda manhã o sistema coleta as notícias do dia, usa o **Opus 4.8** (via OpenRouter)
para escrever uma narrativa-radar e envia tudo (resumo + links) para o **Telegram**.

Roda de graça no **GitHub Actions** — não precisa do seu PC ligado.

## Como funciona

```
GitHub Actions (cron, toda manhã)
   └─ radar.py
        1. Coleta o Google Notícias (RSS gratuito, sem chave)
        2. Deduplica
        3. Opus 4.8 via OpenRouter escreve o "radar"
        4. Envia narrativa + links ao Telegram
```

## Configuração (3 segredos)

Você precisa cadastrar 3 segredos no repositório. Em
**Settings → Secrets and variables → Actions → New repository secret**:

| Segredo | Como obter |
|---|---|
| `TELEGRAM_BOT_TOKEN` | No Telegram, fale com **@BotFather** → `/newbot` → escolha nome/usuário → ele te dá o **token**. |
| `TELEGRAM_CHAT_ID` | Mande qualquer mensagem ao seu bot, depois abra `https://api.telegram.org/bot<SEU_TOKEN>/getUpdates` no navegador e copie o número em `chat.id`. |
| `OPENROUTER_API_KEY` | Crie a chave em **openrouter.ai → Keys**. |

## Testar agora (sem esperar a manhã)

Depois de cadastrar os 3 segredos:

1. Vá na aba **Actions** do repositório.
2. Escolha o workflow **Radar do Orçamento**.
3. Clique em **Run workflow** (botão à direita).

Em ~1 minuto a mensagem deve chegar no seu Telegram.

## Rodar localmente (opcional)

```bash
pip install -r requirements.txt
export OPENROUTER_API_KEY="..."
export TELEGRAM_BOT_TOKEN="..."
export TELEGRAM_CHAT_ID="..."
python radar.py
```

## Ajustes

- **Horário:** edite o `cron` em `.github/workflows/radar.yml` (está em UTC; 12:00 UTC = 09:00 BRT).
- **Termos de busca / nº de notícias:** edite `TERMOS_BUSCA` e `MAX_NOTICIAS` em `radar.py`.
- **Modelo:** o padrão é `anthropic/claude-opus-4.8`; confirme o slug exato em
  [openrouter.ai/models](https://openrouter.ai/models) e ajuste `OPENROUTER_MODEL` se preciso.

## Metodologia

O projeto foi estruturado seguindo o **CRISP-DM** — os entregáveis de cada fase
estão em [`crisp-dm/`](crisp-dm/), e o estado do projeto em
[`crisp-dm/PROGRESSO.md`](crisp-dm/PROGRESSO.md).

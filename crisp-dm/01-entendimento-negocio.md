# Entendimento do Negócio — Curadoria de Notícias de Orçamento

> Status: **em andamento** — Tarefa 1.1 concluída; 1.2 a 1.4 pendentes.

## Contexto
Projeto pessoal de **curadoria automatizada de notícias sobre orçamento público federal**. Hoje não existe nenhuma solução em uso. A ideia é eliminar o garimpo manual de notícias: o sistema coleta, seleciona as relevantes e entrega um resumo diário. A entrega é um **HTML enviado via Telegram**, uma vez por dia, pela manhã, para um único destinatário (o próprio dono do projeto).

## Objetivos de negócio
- **Objetivo primário:** manter-se atualizado diariamente sobre notícias de orçamento público federal, sem esforço manual de busca.
- **Objetivos secundários:** _(a levantar — ex: arquivar histórico, identificar temas recorrentes)_
- **Objetivos rejeitados:** _(nenhum registrado até agora)_

## Critérios de sucesso de negócio
- Receber, **toda manhã**, uma seleção de notícias **realmente relevantes** sobre orçamento público federal.
- **Sem repetição** (mesma notícia não aparece duas vezes) e **sem ruído** (notícias fora do tema).
- **Quem julga:** o próprio dono do projeto (critério subjetivo de satisfação pessoal).

## Inventário de recursos
- **Execução/deploy:** ambiente gratuito, sem depender do PC do dono. **Decisão: GitHub Actions** (cron agendado, gratuito, já temos o repositório).
- **Fontes de dados:** Google / Google Notícias (via Search API ou RSS gratuito do Google News).
- **LLM:** Opus mais recente (`claude-opus-4-8`) via **OpenRouter**.
- **Entrega:** bot do Telegram (a criar).

## Requisitos, premissas e restrições
- **Requisito de prazo:** tem que funcionar **hoje**.
- **Premissa:** custo de LLM é desprezível (centavos/dia para ~5–15 notícias).
- **Restrições:** o mais gratuito possível; não rodar no PC do dono.

## Riscos e contingências
| Risco | Contingência |
|-------|--------------|
| Fonte de notícias bloquear scraping / API esgotar cota grátis | Usar RSS gratuito do Google News (sem chave, ilimitado) |
| Cron do GitHub Actions atrasar/pular execução | Tolerável (não é crítico); reexecução manual disponível |
| Chave de API exposta | Guardar tudo em GitHub Actions Secrets (nunca no código) |

## Terminologia
- **Radar:** narrativa-resumo diária gerada pelo LLM a partir das notícias do dia.
- **Curadoria:** seleção das notícias relevantes (filtra ruído e repetição).

## Custos e benefícios
- **Custos:** ~centavos/dia de tokens do LLM (OpenRouter). GitHub Actions e RSS gratuitos.
- **Benefícios:** estar atualizado diariamente sobre orçamento público federal sem esforço manual.

## Metas de mineração de dados
- **Tipo de problema:** seleção/classificação de relevância + sumarização (descrição/sumarização).
- **Meta técnica:** dado o conjunto de notícias coletadas no dia sobre "orçamento público federal", produzir (a) uma narrativa-radar coesa e (b) a lista de links das notícias relevantes, sem repetição.

## Critérios de sucesso de dados
- A narrativa cobre as notícias do dia sem inventar fatos (sem alucinação).
- Sem duplicatas; sem itens fora do tema "orçamento público federal".
- Saída entregue no Telegram toda manhã.

## Plano do projeto (pipeline)
1. **Coletar** notícias do dia (Google Notícias) sobre orçamento público federal.
2. **Deduplicar** por título/URL.
3. **Curar + narrar** com Opus 4.8 (OpenRouter): seleciona relevantes e escreve o "radar".
4. **Formatar** saída (mensagem HTML no Telegram + links; PDF como evolução).
5. **Enviar** ao Telegram (1 destinatário) — agendado via GitHub Actions, 1x/manhã.

## Avaliação inicial de ferramentas e técnicas
- **Linguagem:** Python.
- **Coleta:** `feedparser` (RSS do Google News) ou Search API.
- **LLM:** OpenRouter → `anthropic/claude-opus-4.8` (confirmar slug no catálogo).
- **Telegram:** API de Bot (`sendMessage` com `parse_mode=HTML`; `sendDocument` se PDF).
- **Agendamento:** GitHub Actions (`schedule: cron`).

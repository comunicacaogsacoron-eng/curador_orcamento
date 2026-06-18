# PROGRESSO — Curadoria de Notícias de Orçamento

> Última atualização: 2026-06-18

## Estado atual
- **Fase:** 1 — Entendimento do Negócio (concluída) → partindo para implementação
- **Tarefa:** montar o pipeline (modo pragmático: "tem que funcionar hoje")
- **Modo de condução:** guiado → acelerado

## Resumo do projeto
- Objetivo de negócio: ficar atualizado diariamente sobre orçamento público federal, sem garimpo manual.
- Tipo de problema: curadoria de conteúdo (seleção/classificação de relevância + sumarização).
- Entrega: HTML via Telegram, 1x/dia pela manhã, para 1 destinatário (o dono).

## Fases e tarefas
- [x] 1. Entendimento do Negócio — concluída
- [~] Implementação do pipeline — em andamento
- [ ] 2–6 (Dados/Preparação/Modelagem/Avaliação/Implantação) — encaixadas na construção

## Entregáveis gerados
- crisp-dm/01-entendimento-negocio.md (completo)

## Pendências (bloqueiam o "funcionar hoje")
- [ ] Criar bot no Telegram (@BotFather) → obter TOKEN e CHAT_ID
- [ ] Obter chave do OpenRouter (OPENROUTER_API_KEY)
- [ ] Confirmar fonte: RSS grátis do Google News (recomendado) vs Search API com chave
- [ ] Cadastrar segredos no GitHub Actions

## Decisões tomadas
- Escopo: orçamento público **federal**. Uso pessoal, destinatário único. 1 envio/manhã.
- **Deploy:** GitHub Actions (gratuito, agendado, não usa o PC).
- **Fonte:** Google Notícias.
- **LLM:** `claude-opus-4-8` (Opus 4.8, mais recente) via OpenRouter.
- **Saída:** narrativa "radar" + links no Telegram (PDF como evolução).

## Próximo passo
Construir o pipeline em Python + workflow do GitHub Actions; usuário providencia os 3 segredos.

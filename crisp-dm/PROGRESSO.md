# PROGRESSO — Curadoria de Notícias de Orçamento

> Última atualização: 2026-06-18

## Estado atual
- **Fase:** 1 — Entendimento do Negócio
- **Tarefa:** 1.2 — Avaliar a situação (em andamento)
- **Modo de condução:** guiado

## Resumo do projeto
- Objetivo de negócio: ficar atualizado diariamente sobre orçamento público federal, sem garimpo manual.
- Tipo de problema: curadoria de conteúdo (seleção/classificação de relevância + sumarização).
- Entrega: HTML via Telegram, 1x/dia pela manhã, para 1 destinatário (o dono).

## Fases e tarefas
- [~] 1. Entendimento do Negócio — em andamento (1.1 ok; 1.2–1.4 pendentes)
- [ ] 2. Entendimento dos Dados
- [ ] 3. Preparação dos Dados
- [ ] 4. Modelagem
- [ ] 5. Avaliação
- [ ] 6. Implantação

## Entregáveis gerados
- crisp-dm/01-entendimento-negocio.md (parcial — só 1.1)

## Pendências
- [ ] Definir fontes de notícias (sites, Diário Oficial, APIs)
- [ ] Definir onde o sistema vai rodar (PC, servidor, nuvem/cron)
- [ ] Definir se haverá uso de LLM/API paga para filtrar/resumir
- [ ] Confirmar se o bot do Telegram já existe

## Decisões tomadas
- Escopo: orçamento público **federal** (não estadual/municipal).
- Uso pessoal, destinatário único.
- Frequência: 1 envio diário pela manhã.

## Próximo passo
Levantar a situação (Tarefa 1.2): recursos, fontes de dados, restrições técnicas/legais, custos.

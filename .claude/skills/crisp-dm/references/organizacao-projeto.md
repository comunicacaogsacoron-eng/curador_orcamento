# Organização do projeto e continuidade entre sessões

Como montar a estrutura do projeto e manter o estado para retomar em sessões futuras. Leia ao iniciar um projeto novo ou ao retomar um existente.

## Estrutura padrão

```
[nome-do-projeto]/
├── crisp-dm/
│   ├── PROGRESSO.md                  ← estado: fase atual, tarefa, pendências, decisões
│   ├── 01-entendimento-negocio.md
│   ├── 02-entendimento-dados.md
│   ├── 03-preparacao-dados.md
│   ├── 04-modelagem.md
│   ├── 05-avaliacao.md
│   └── 06-implantacao.md
├── data/
│   ├── raw/                          ← dados brutos, nunca editados
│   └── processed/                    ← datasets preparados (saída da Fase 3)
└── notebooks/                        ← análises, scripts, experimentos
```

Os 6 arquivos de fase começam vazios (ou só com o cabeçalho do template) e vão sendo preenchidos conforme o projeto avança. Não é preciso criar os 6 de uma vez; pode criar cada um quando a fase chegar. O `PROGRESSO.md` é criado já no início.

## Ao iniciar um projeto novo

1. Confirme o **nome do projeto** com o usuário.
2. Confirme a estrutura (o usuário pode já ter pastas `data/`/`notebooks/` próprias — respeite-as).
3. Crie a pasta `crisp-dm/` e o `PROGRESSO.md` inicial.
4. Em ambiente com arquivos persistentes (Claude Code), crie tudo no diretório do projeto. No chat, crie em `/mnt/user-data/outputs/`.

## Ao retomar um projeto (início de cada sessão)

**Sempre leia `crisp-dm/PROGRESSO.md` primeiro**, antes de perguntar qualquer coisa. Ele diz em que fase/tarefa o projeto está, o que ficou pendente e que decisões já foram tomadas. Depois de ler, confirme com o usuário ("Pelo PROGRESSO, paramos na Fase 3, tarefa 3.2, com X pendente — seguimos daí?") e continue.

No chat web/desktop, como os arquivos não persistem, peça ao usuário para reanexar o `PROGRESSO.md` (e os entregáveis relevantes) no início da conversa. Se ele não tiver, reconstrua o estado perguntando onde parou.

## Regras de atualização do PROGRESSO.md

Atualize o `PROGRESSO.md` ao final de **cada tarefa concluída** (não só ao fim da fase). Registre: tarefa concluída, entregável gerado, pendências abertas e qualquer decisão importante. É isso que torna a retomada confiável.

## Template — PROGRESSO.md

```markdown
# PROGRESSO — [Nome do Projeto]

> Última atualização: [data/sessão]

## Estado atual
- **Fase:** [ex: 3 — Preparação dos Dados]
- **Tarefa:** [ex: 3.2 — Limpar dados]
- **Modo de condução:** [guiado / consultivo]

## Resumo do projeto
- Objetivo de negócio: [uma linha]
- Tipo de problema: [classificação / predição / ...]
- Meta de dados: [uma linha]

## Fases e tarefas
- [x] 1. Entendimento do Negócio — concluída
- [~] 2. Entendimento dos Dados — em andamento (falta verificar qualidade)
- [ ] 3. Preparação dos Dados
- [ ] 4. Modelagem
- [ ] 5. Avaliação
- [ ] 6. Implantação

## Entregáveis gerados
- crisp-dm/01-entendimento-negocio.md ✓
- crisp-dm/02-entendimento-dados.md (parcial)

## Pendências
- [ ] [ex: confirmar permissão de uso dos dados de cobrança]
- [ ] [ex: definir critério de sucesso de dados — quem julga?]

## Decisões tomadas
- [ex: excluir clientes com < 3 meses de base — pré-pagos têm churn diferente]
- [ex: usar 12 meses de histórico, não 18]

## Próximo passo
[ex: terminar tarefa 2.4 (qualidade dos dados) e gerar relatório da Fase 2]
```

Mantenha o `PROGRESSO.md` curto e factual — é um índice de estado, não um diário. O detalhe vai nos entregáveis de cada fase.

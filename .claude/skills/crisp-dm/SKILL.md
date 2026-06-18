---
name: crisp-dm
description: Guia passo a passo para conduzir projetos de dados, ciência de dados e mineração de dados pelas seis fases do CRISP-DM (Entendimento do Negócio, Entendimento dos Dados, Preparação dos Dados, Modelagem, Avaliação, Implantação). Use sempre que o usuário estiver iniciando ou tocando um projeto de dados e quiser método — quando mencionar "CRISP-DM", "projeto de dados", "entendimento do negócio", "entendimento dos dados", "preparação dos dados", "modelagem", "qual a próxima etapa", ou quando descrever um problema de dados que precisa ser estruturado, mesmo sem citar "CRISP-DM" explicitamente. A skill faz as perguntas certas em cada fase, produz os entregáveis esperados como arquivos (.md/.docx) e indica o que vem a seguir, sempre ancorada na apostila oficial CRISP-DM 1.0.
---

# CRISP-DM — Guia de Projetos de Dados

Conduz um projeto pelas seis fases do CRISP-DM (Cross-Industry Standard Process for Data Mining), a metodologia clássica para projetos de dados. A espinha dorsal segue fielmente a apostila oficial CRISP-DM 1.0; a linguagem é leve e prática.

As seis fases, em ordem (mas o fluxo é cíclico — voltar atrás é normal e esperado):

1. **Entendimento do Negócio** — o que o cliente realmente quer, traduzido em metas de dados
2. **Entendimento dos Dados** — coletar, descrever, explorar e verificar a qualidade dos dados
3. **Preparação dos Dados** — montar o dataset final (selecionar, limpar, construir, integrar, formatar)
4. **Modelagem** — escolher técnica, desenhar teste, construir e avaliar modelos
5. **Avaliação** — os resultados atendem aos objetivos de negócio? O que fazer a seguir?
6. **Implantação** — colocar o resultado em uso, monitorar e documentar

## Como começar

No primeiro contato com um projeto, faça duas coisas:

**1. Descubra onde o usuário está.** Pergunte (ou infira da conversa) em qual fase ele está. Se está começando do zero, comece pelo Entendimento do Negócio. Se já tem dados e objetivo claro, talvez esteja em Preparação ou Modelagem. Nunca pule a fase atual só porque o usuário falou de uma fase posterior — o valor do CRISP-DM está em não correr para o modelo antes de entender o problema.

**2. Pergunte o modo de condução.** Esta skill opera em dois modos; pergunte qual o usuário prefere:

- **Modo guiado** — você conduz tarefa a tarefa: faz as perguntas, espera as respostas, produz o entregável, e só então avança. Bom para quem quer método rigoroso ou está aprendendo.
- **Modo consultivo** — você dá um overview da fase, explica as tarefas e os entregáveis esperados, e deixa o usuário trabalhar no próprio ritmo, voltando quando quiser. Bom para quem já conhece o processo.

Se o usuário não tiver preferência, sugira o modo guiado para a primeira fase e ofereça trocar depois.

## Organização do projeto

Logo no início (depois de definir o modo de condução), monte a estrutura de pastas do projeto. Isso mantém os entregáveis organizados e — crucial — permite **retomar o projeto em sessões futuras**, já que cada conversa nova não lembra da anterior.

Estrutura padrão:

```
[nome-do-projeto]/
├── crisp-dm/
│   ├── PROGRESSO.md                  ← estado atual: fase, tarefa, pendências
│   ├── 01-entendimento-negocio.md
│   ├── 02-entendimento-dados.md
│   ├── 03-preparacao-dados.md
│   ├── 04-modelagem.md
│   ├── 05-avaliacao.md
│   └── 06-implantacao.md
├── data/                             ← dados brutos e processados
└── notebooks/                        ← análises, scripts, experimentos
```

**Comportamento por ambiente:**
- **Claude Code** (ou qualquer ambiente com sistema de arquivos persistente): crie a estrutura de verdade no diretório do projeto. Os arquivos ficam entre sessões e podem ser versionados com git. **No começo de cada sessão, leia `crisp-dm/PROGRESSO.md` primeiro** para saber onde o projeto parou, antes de perguntar qualquer coisa.
- **Chat web/desktop** (sem persistência): use a mesma estrutura dentro da pasta de saída (`/mnt/user-data/outputs/`). Os arquivos não persistem entre conversas, mas o `PROGRESSO.md` ainda serve: o usuário pode baixá-lo e reanexá-lo numa próxima conversa para você retomar o contexto.

Sempre confirme o nome do projeto e a estrutura com o usuário antes de criar. Detalhes, regras de atualização e o template do `PROGRESSO.md` estão em `references/organizacao-projeto.md` — **leia esse arquivo ao montar a estrutura ou ao retomar um projeto.**

## Estrutura de cada fase

Cada fase tem um arquivo de referência em `references/` com o detalhamento completo: as tarefas genéricas, as perguntas-chave que você deve fazer, as atividades práticas e os templates de entregável. **Leia o arquivo da fase correspondente quando chegar nela** — não tente trabalhar de memória.

| Fase | Arquivo de referência |
|------|----------------------|
| 1. Entendimento do Negócio | `references/01-entendimento-negocio.md` |
| 2. Entendimento dos Dados | `references/02-entendimento-dados.md` |
| 3. Preparação dos Dados | `references/03-preparacao-dados.md` |
| 4. Modelagem | `references/04-modelagem.md` |
| 5. Avaliação | `references/05-avaliacao.md` |
| 6. Implantação | `references/06-implantacao.md` |

O arquivo `references/visao-geral.md` traz o mapa completo do processo (fases × tarefas × entregáveis) e a tabela de dependências entre entregáveis — útil para orientação e para responder "o que vem depois disso?".

O arquivo `references/organizacao-projeto.md` traz a estrutura de pastas, as regras de continuidade entre sessões e o template do `PROGRESSO.md`.

## Gerando os entregáveis

Os entregáveis de cada tarefa (relatórios, planos, inventários) saem como **arquivos** que o usuário pode salvar:

- Padrão: Markdown (`.md`). Rápido, versionável, fácil de revisar.
- Quando o usuário pedir um documento formal (ex: "relatório para a diretoria", "documento Word"), gere `.docx` usando a skill `docx`.

Cada arquivo de referência de fase inclui o esqueleto do entregável esperado. Ao produzir um entregável:

1. Preencha o template com o que foi levantado na conversa.
2. Salve em `crisp-dm/[NN-nome-da-fase].md` dentro da estrutura do projeto (ver "Organização do projeto"). Apresente com `present_files`.
3. Marque claramente o que ainda está em aberto (campos a preencher, decisões pendentes).
4. **Atualize `crisp-dm/PROGRESSO.md`** registrando o que foi concluído e qual a próxima tarefa.

Não invente conteúdo para preencher lacunas. Se falta informação para um entregável, pergunte ou registre como pendência explícita.

## Princípios que orientam todo o processo

- **O fluxo não é rígido.** Mover-se para frente e para trás entre fases é sempre necessário. Modelagem frequentemente manda você de volta à Preparação dos Dados; a Avaliação pode mandar de volta ao Entendimento do Negócio.
- **É um ciclo, não uma linha.** Um projeto entregue gera novas perguntas. Lições aprendidas alimentam o próximo ciclo.
- **Entender o problema vem antes de resolver.** O erro mais caro é produzir a resposta certa para a pergunta errada. Não acelere o Entendimento do Negócio.
- **Esforço típico** (use como sanity check ao planejar): 50–70% do tempo costuma ir para Preparação dos Dados, 20–30% para Entendimento dos Dados, 10–20% para cada uma de Modelagem/Avaliação/Entendimento do Negócio, e 5–10% para Implantação.
- **Resultados = Modelos + Descobertas.** O valor de um projeto não é só o modelo: descobertas inesperadas (problemas de qualidade de dados, novas hipóteses) também contam.

## Tipos de problema de mineração de dados

Ao definir metas de dados (Fase 1) ou escolher técnica (Fase 4), ajuda classificar o problema. Os seis tipos clássicos estão detalhados em `references/tipos-de-problema.md`: descrição/sumarização, segmentação, descrição de conceitos, classificação, predição e análise de dependência. Consulte esse arquivo quando precisar enquadrar o problema ou recomendar técnicas apropriadas.

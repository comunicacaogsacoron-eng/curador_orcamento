# Fase 1 — Entendimento do Negócio

A fase mais importante e a mais negligenciada. O objetivo é entender, da perspectiva do negócio, o que o cliente realmente quer — e traduzir isso em um problema de dados bem definido e um plano. O erro clássico aqui é gastar esforço produzindo a resposta certa para a pergunta errada.

Quatro tarefas: determinar objetivos de negócio → avaliar a situação → determinar metas de dados → produzir plano do projeto.

---

## 1.1 Determinar objetivos de negócio

Entender o que o cliente quer realizar. Normalmente há objetivos e restrições concorrentes que precisam ser balanceados.

**Perguntas-chave:**
- Qual é o objetivo primário do negócio, em termos de negócio (não técnicos)?
- Quais perguntas de negócio secundárias o cliente também quer responder?
- Quem são as pessoas-chave, o patrocinador, os usuários do resultado?
- Existe solução atual para o problema? Quais suas vantagens e limitações?
- Como será o sucesso, do ponto de vista do negócio? Quem julga isso?

**Cuidado:** não estabeleça metas inatingíveis. Cada critério de sucesso deve se ligar a pelo menos um objetivo de negócio.

**Entregáveis:** Contexto (background), Objetivos de negócio, Critérios de sucesso de negócio.

---

## 1.2 Avaliar a situação

Levantamento mais detalhado de recursos, restrições, premissas e outros fatores.

**Perguntas-chave:**
- **Recursos:** que pessoal (especialistas de negócio e de dados, suporte técnico), dados (extrações fixas, acesso a base viva), hardware e software estão disponíveis?
- **Requisitos:** prazo, comprensibilidade e qualidade exigida, segurança, questões legais. *Você tem permissão para usar os dados?*
- **Premissas:** quais suposições o projeto faz (sobre dados e sobre o negócio)? Liste sobretudo as que condicionam a validade dos resultados.
- **Restrições:** de recursos, de acesso aos dados, técnicas (ex: volume de dados viável), legais.
- **Riscos:** que eventos podem atrasar ou inviabilizar o projeto? Qual o plano de contingência?
- **Terminologia:** glossário de termos de negócio + termos de mineração de dados.
- **Custos e benefícios:** análise comparando custo do projeto com o benefício potencial, o mais concreta possível.

**Cuidado:** lembre dos custos ocultos — extração e preparação repetidas, mudanças de fluxo de trabalho, tempo de treinamento.

**Entregáveis:** Inventário de recursos, Requisitos/premissas/restrições, Riscos e contingências, Terminologia, Custos e benefícios.

---

## 1.3 Determinar metas de mineração de dados

Uma meta de negócio é dita em termos de negócio; uma meta de dados, em termos técnicos. Ex: objetivo de negócio = "aumentar vendas do catálogo para clientes atuais"; meta de dados = "prever quantas unidades um cliente comprará, dado seu histórico de 3 anos, dados demográficos e o preço do item".

**Perguntas-chave:**
- Como traduzir cada pergunta de negócio em uma meta técnica de dados?
- Qual o tipo de problema de dados? (classificação, descrição, predição, segmentação… ver `tipos-de-problema.md`)
- Quais critérios técnicos definem sucesso? (ex: nível de acurácia, lift)

**Cuidado:** os critérios de sucesso de dados são diferentes dos critérios de sucesso de negócio. Às vezes vale redefinir o problema (ex: modelar retenção de produto em vez de retenção de cliente).

**Entregáveis:** Metas de dados, Critérios de sucesso de dados.

---

## 1.4 Produzir plano do projeto

Plano para atingir as metas de dados e, com isso, as metas de negócio.

**Perguntas-chave:**
- Quais as etapas, com duração, recursos, insumos, saídas e dependências?
- Onde estão as grandes iterações (ex: repetir modelagem ↔ avaliação)?
- Quais as dependências entre cronograma e riscos?
- Que ferramentas e técnicas usar inicialmente? (avaliação preliminar)

O plano é um documento vivo: revise ao fim de cada fase. Lembre da distribuição típica de esforço (Preparação dos Dados costuma consumir 50–70%).

**Entregáveis:** Plano do projeto, Avaliação inicial de ferramentas e técnicas.

---

## Template de entregável — Relatório de Entendimento do Negócio

```markdown
# Entendimento do Negócio — [Nome do Projeto]

## Contexto
[Onde o projeto se insere, problema identificado, por que dados ajudam]

## Objetivos de negócio
- Objetivo primário:
- Objetivos secundários:
- Objetivos considerados e rejeitados (com motivo):

## Critérios de sucesso de negócio
- [Critério mensurável ou subjetivo — se subjetivo, quem julga]

## Inventário de recursos
- Pessoal:
- Dados:
- Hardware/Software:

## Requisitos, premissas e restrições
- Requisitos:
- Premissas:
- Restrições:

## Riscos e contingências
| Risco | Contingência |
|-------|--------------|

## Terminologia
[Glossário de negócio + de dados]

## Custos e benefícios
- Custos:
- Benefícios esperados:

## Metas de mineração de dados
- Tipo de problema:
- Metas técnicas:

## Critérios de sucesso de dados
- [Critérios técnicos]

## Plano do projeto
| Etapa | Duração | Recursos | Insumos | Saídas | Dependências |
|-------|---------|----------|---------|--------|--------------|

## Avaliação inicial de ferramentas e técnicas
[Ferramentas/técnicas candidatas e adequação]
```

**Próxima fase:** Entendimento dos Dados (`02-entendimento-dados.md`).

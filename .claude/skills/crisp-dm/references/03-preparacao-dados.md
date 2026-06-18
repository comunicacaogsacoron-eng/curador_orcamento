# Fase 3 — Preparação dos Dados

Cobre tudo que é preciso para construir o dataset final (o que será alimentado nas ferramentas de modelagem) a partir dos dados brutos. É a fase que mais consome tempo (tipicamente 50–70% do projeto). As tarefas se repetem várias vezes e não seguem ordem prescrita.

Cinco tarefas: selecionar → limpar → construir → integrar → formatar.

> Em qualquer tarefa, é comum reconsiderar os critérios de seleção de dados à luz do que se aprende (qualidade, exploração, modelagem). Voltar atrás aqui é a regra, não a exceção.

---

## 3.1 Selecionar dados

Decidir quais dados usar. Critérios: relevância para as metas, qualidade, restrições técnicas (volume, tipos). Cobre seleção de atributos (colunas) e de registros (linhas).

**Perguntas-chave:**
- Quais atributos são necessários? Quais foram identificados como irrelevantes? Quantos a técnica aguenta?
- Vale usar amostragem (reduzir tamanho, dividir treino/teste, amostras ponderadas)?
- Algum atributo é mais importante que outros e deve ser ponderado?

**Entregável:** Justificativa de inclusão/exclusão — o que entra/sai e por quê.

---

## 3.2 Limpar dados

Elevar a qualidade ao nível exigido pela técnica escolhida: subconjuntos limpos, inserção de defaults, ou estimativa de ausentes por modelagem.

**Perguntas-chave:**
- Como tratar o ruído detectado (corrigir, remover, ignorar)?
- Como tratar valores especiais e seus significados?
- Que problemas de qualidade permanecem e como afetam os resultados?

**Cuidado:** se ignorar ruído em campos irrelevantes, documente — as circunstâncias podem mudar depois.

**Entregável:** Relatório de limpeza — decisões e ações tomadas frente aos problemas do relatório de qualidade.

---

## 3.3 Construir dados

Operações construtivas: atributos derivados, novos registros, valores transformados.

**Perguntas-chave:**
- Que atributos derivados fazem sentido? (ex: área = comprimento × largura; "renda per capita")
- Algum atributo precisa ser normalizado (ex: clustering com idade e renda)?
- Como construir/imputar atributos ausentes (agregação, média, indução)?
- Precisa de transformações de atributo único (ex: faixas → símbolos, símbolos → numérico)?
- Precisa gerar registros novos (ex: protótipo de cada segmento; registro de "zero compras")?

**Cuidado:** antes de derivar, verifique se de fato facilita o modelo. Não derive só para reduzir o nº de atributos.

**Entregáveis:** Atributos derivados, Registros gerados.

---

## 3.4 Integrar dados

Combinar informação de múltiplas tabelas/fontes para criar novos registros ou valores.

**Perguntas-chave:**
- Que tabelas mesclar (join) — informações diferentes sobre os mesmos objetos?
- Que agregações computar (ex: de uma linha por compra para uma linha por cliente, com nº de compras, valor médio etc.)?
- As ferramentas de integração dão conta das fontes como estão?

**Entregável:** Dados mesclados (merges e agregações).

---

## 3.5 Formatar dados

Modificações primariamente sintáticas que não mudam o significado, mas são exigidas pela ferramenta de modelagem.

**Perguntas-chave:**
- A ferramenta exige ordem específica de atributos (ex: 1º campo = ID, último = alvo)?
- Precisa reordenar registros (ex: ordenar por alvo, ou randomizar para redes neurais)?
- Há ajustes sintáticos (remover vírgulas de campos texto, truncar a N caracteres)?

**Entregável:** Dados reformatados.

---

## Saídas gerais da fase

- **Dataset** — o(s) conjunto(s) de dados que irá(ão) para a modelagem.
- **Descrição do dataset** — descrição do dataset resultante.

## Template de entregável — Preparação dos Dados

```markdown
# Preparação dos Dados — [Nome do Projeto]

## Justificativa de inclusão/exclusão
- Dados/atributos incluídos e por quê:
- Dados/atributos excluídos e por quê:

## Relatório de limpeza
- Problemas de qualidade tratados e como:
- Tratamento de valores especiais e ruído:
- Pendências e possíveis impactos nos resultados:

## Construção de dados
- Atributos derivados (definição e motivo):
- Transformações de atributo único:
- Registros gerados:

## Integração de dados
- Tabelas mescladas (joins):
- Agregações computadas:

## Formatação
- Reordenação de atributos/registros:
- Ajustes sintáticos:

## Descrição do dataset final
- Pré-processamento aplicado:
- Descrição tabela a tabela / campo a campo:
- Descobertas durante o pré-processamento e implicações:
```

**Próxima fase:** Modelagem (`04-modelagem.md`). Espere voltar aqui várias vezes durante a modelagem.

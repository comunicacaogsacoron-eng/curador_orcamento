# Fase 2 — Entendimento dos Dados

Começa com a coleta inicial e segue com atividades para se familiarizar com os dados, identificar problemas de qualidade, ter os primeiros insights e detectar subconjuntos interessantes que sugiram hipóteses.

Quatro tarefas: coletar dados iniciais → descrever → explorar → verificar qualidade. (A ordem é flexível e iterativa.)

---

## 2.1 Coletar dados iniciais

Adquirir os dados (ou acesso a eles) listados nos recursos do projeto, incluindo o carregamento se necessário.

**Perguntas-chave:**
- Quais fontes de dados existem e de que tipo (online, especialistas, documentos)?
- Toda a informação necessária para as metas de dados está disponível?
- Como extrair os dados? Há conhecimento em fontes não eletrônicas (pessoas, papel)?
- Há múltiplas fontes? Então a integração vira uma questão (aqui ou na Preparação).

**Cuidado:** dados de fontes diferentes podem gerar problemas de qualidade ao serem mesclados (formatos inconsistentes, dados inválidos).

**Entregável:** Relatório de coleta inicial — datasets adquiridos, localização, método de aquisição, problemas encontrados e soluções (para replicação futura).

---

## 2.2 Descrever os dados

Examinar as propriedades "de superfície" dos dados.

**Perguntas-chave:**
- Qual o formato e a quantidade (nº de registros e campos por tabela)?
- Quais os atributos, seus tipos (numérico, simbólico, taxonomia) e faixas de valor?
- Estatísticas básicas por atributo (distribuição, média, máx, mín, desvio, moda)?
- O que cada atributo significa em termos de negócio? É relevante para a meta?
- Os dados adquiridos satisfazem os requisitos?

**Entregável:** Relatório de descrição dos dados.

---

## 2.3 Explorar os dados

Atacar questões via consulta, visualização e relatório: distribuição de atributos-chave, relações entre pares de atributos, agregações simples, sub-populações, análises estatísticas simples.

**Perguntas-chave:**
- Como se distribui o atributo-alvo? Que relações aparecem entre atributos?
- Que sub-populações são interessantes?
- Que primeiras hipóteses surgem e como impactam o resto do projeto?
- Dá para transformar alguma hipótese em (ou refinar) uma meta de dados?

**Entregável:** Relatório de exploração — primeiros achados, hipóteses, gráficos relevantes.

---

## 2.4 Verificar a qualidade dos dados

Examinar se os dados estão completos, corretos e como tratam valores ausentes.

**Perguntas-chave:**
- Os dados cobrem todos os casos necessários (completude)?
- Há erros? Quão comuns? Há valores ausentes — como representados, onde, quão frequentes?
- Há valores especiais (ex: '99' para desconhecido, '00' truncado)? O que significam?
- Atributos com valores diferentes e significados parecidos (ex: "light", "diet")?
- Inconsistências de grafia, desvios (ruído vs. fenômeno interessante), valores implausíveis (ex: adolescente com renda alta)?
- Em arquivos planos: o delimitador é consistente? O nº de campos por registro bate?

**Entregável:** Relatório de qualidade dos dados — resultados da verificação e, se houver problemas, possíveis soluções.

---

## Template de entregável — Relatórios de Entendimento dos Dados

```markdown
# Entendimento dos Dados — [Nome do Projeto]

## Relatório de coleta inicial
- Fontes de dados (área coberta por cada):
- Método de aquisição/extração por fonte:
- Problemas encontrados e soluções:

## Relatório de descrição dos dados
- Fontes descritas em detalhe:
- Tabelas/objetos:
- Campos (unidades, códigos, tipos, faixas):
- Estatísticas básicas e significado de negócio:

## Relatório de exploração dos dados
- Objetivos da exploração:
- Padrões esperados × encontrados (esperados e inesperados):
- Conclusões para transformação/limpeza/pré-processamento:
- Conclusões para metas de dados / objetivos de negócio:

## Relatório de qualidade dos dados
- Abordagem de avaliação de qualidade:
- Resultados (completude, erros, ausentes, valores especiais):
- Problemas em aberto e possíveis soluções:
```

**Observação:** estes relatórios idealmente são escritos enquanto as tarefas são executadas. Voltar ao Entendimento do Negócio para ajustar metas é comum nesta fase.

**Próxima fase:** Preparação dos Dados (`03-preparacao-dados.md`).

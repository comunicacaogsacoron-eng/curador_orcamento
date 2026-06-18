# Fase 4 — Modelagem

Selecionar e aplicar técnicas de modelagem, calibrando parâmetros. Há tipicamente várias técnicas para o mesmo tipo de problema, e algumas têm exigências específicas sobre a forma dos dados — por isso voltar à Preparação dos Dados é frequente.

Quatro tarefas: selecionar técnica → gerar desenho de teste → construir modelo → avaliar modelo.

---

## 4.1 Selecionar técnica de modelagem

Escolher a técnica concreta (ex: árvore de decisão com C4.5, rede neural com retropropagação). Se usar várias técnicas, faça esta tarefa para cada uma.

**Perguntas-chave:**
- Que técnica é apropriada para o tipo de problema? (ver `tipos-de-problema.md`)
- Que restrições limitam a escolha (ferramenta disponível, "requisitos políticos" como comprensibilidade exigida pela gestão, tempo, conhecimento da equipe)?
- Que premissas a técnica faz sobre os dados (distribuição, ausentes, tipo do alvo)? Elas se sustentam frente ao relatório de descrição dos dados?

**Cuidado:** nem toda técnica serve para toda tarefa. Compare as premissas com a realidade dos dados e, se preciso, volte à Preparação.

**Entregáveis:** Técnica de modelagem, Premissas de modelagem.

---

## 4.2 Gerar desenho de teste

Definir, antes de construir, como testar a qualidade e a validade do modelo. Em tarefas supervisionadas (ex: classificação), é comum separar treino/teste, construir no treino e estimar a qualidade no teste.

**Perguntas-chave:**
- Como dividir o dataset em treino, teste e validação?
- Que medida de qualidade usar (ex: taxa de erro)?
- Quantas iterações/folds? Precisa preparar dados específicos para o teste?

**Entregável:** Desenho de teste.

---

## 4.3 Construir modelo

Rodar a ferramenta no dataset preparado para gerar um ou mais modelos.

**Perguntas-chave:**
- Quais parâmetros ajustar e com que valores (e por quê)?
- Como pós-processar os resultados (editar regras, exibir árvores)?
- Como interpretar o modelo resultante? Acurácia esperada, robustez, limitações?

**Entregáveis:**
- Configurações de parâmetros (valores escolhidos + justificativa)
- Modelos (os modelos em si, não um relatório)
- Descrição do modelo (interpretação, regras produzidas, topologia para modelos opacos, conclusões sobre padrões nos dados)

---

## 4.4 Avaliar modelo

Avaliação **técnica** — verificar se o modelo atende aos critérios de sucesso de dados e passa nos critérios de teste. (A avaliação frente ao negócio é a Fase 5.)

**Perguntas-chave:**
- Como os modelos se classificam entre si segundo os critérios de avaliação?
- O resultado é plausível, confiável, novo e útil? Sobrevive ao olhar de especialistas?
- Que parâmetros revisar para a próxima rodada de construção?

Itere construção ↔ avaliação até acreditar fortemente que encontrou o(s) melhor(es) modelo(s). Ferramentas como "lift tables" e "gain tables" ajudam a medir desempenho preditivo.

**Entregáveis:** Avaliação do modelo (qualidades e ranking), Configurações revisadas de parâmetros.

---

## Template de entregável — Modelagem

```markdown
# Modelagem — [Nome do Projeto]

## Premissas de modelagem
[Premissas sobre dados, explícitas e implícitas na técnica]

## Desenho de teste
- Tipo de modelo e dados de treino:
- Como o modelo será testado/avaliado:
- Divisão treino/teste/validação:

## Descrição do modelo
Para cada modelo:
- Tipo e relação com as metas de dados:
- Configurações de parâmetros usadas:
- Descrição detalhada e características especiais:
- (regras produzidas / topologia, se aplicável)
- Comportamento e interpretação:
- Conclusões sobre padrões nos dados:

## Avaliação do modelo
Para cada modelo:
- Avaliação detalhada (acurácia, interpretação):
- Comentários de especialistas:
- Ranking frente aos critérios de sucesso:
- Por que tal técnica/parâmetros deram bom/mau resultado:
- Configurações revisadas para a próxima rodada:
```

**Próxima fase:** Avaliação (`05-avaliacao.md`) — agora frente aos objetivos de negócio. Mas pode ser que você volte à Preparação dos Dados antes.

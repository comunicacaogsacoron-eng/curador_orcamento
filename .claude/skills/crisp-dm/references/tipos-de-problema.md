# Tipos de problema de mineração de dados

Um projeto normalmente combina vários tipos de problema para resolver a questão de negócio. Use esta classificação ao definir metas de dados (Fase 1) ou escolher técnica (Fase 4). Os seis tipos clássicos:

---

## 1. Descrição e sumarização dos dados
Descrição concisa das características dos dados, em forma elementar e agregada — dá uma visão geral da estrutura. Às vezes é objetivo em si (ex: faturamento por categoria, com comparação a período anterior), mas quase sempre aparece como sub-meta nas fases iniciais, ajudando a entender a natureza dos dados e levantar hipóteses. É a tarefa central do Entendimento dos Dados. Ferramentas: relatórios, pacotes estatísticos, OLAP, EIS.

## 2. Segmentação
Separar os dados em subgrupos interessantes e significativos, cujos membros compartilham características. Pode ser objetivo próprio ou um passo para outros tipos (manter o tamanho gerenciável, achar subconjuntos homogêneos mais fáceis de analisar). Pode ser manual (hipóteses prévias) ou automática (clustering descobre estruturas ocultas).
**Nota terminológica:** segmentação é às vezes chamada de "clustering" ou (de forma confusa) "classificação". Aqui, segmentação = criar as classes; classificação = prever classes conhecidas para casos novos.
**Técnicas:** clustering, redes neurais, visualização.
*Ex: dividir clientes por características socioeconômicas e desenhar estratégias de marketing por grupo.*

## 3. Descrição de conceitos
Descrição compreensível de conceitos ou classes — o foco é ganhar insight, não acurácia preditiva. Ligada à segmentação (que enumera objetos sem descrevê-los) e à classificação (que pode produzir descrições). Diferença importante: classificação precisa ser completa (aplicar a todos os casos); descrição de conceitos não — basta descrever partes importantes.
**Técnicas:** indução de regras, clustering conceitual.
*Ex: gerar regras que descrevem clientes leais × desleais para entender o que os diferencia.*

## 4. Classificação
Há objetos caracterizados por atributos que pertencem a classes diferentes; o rótulo da classe é discreto (simbólico) e conhecido para cada objeto. O objetivo é construir um modelo (classificador) que atribua o rótulo correto a objetos novos e não rotulados. Um dos tipos mais importantes e comuns; muitos problemas se transformam em classificação (ex: credit scoring → bom/mau cliente). Problemas de predição viram classificação ao "binar" rótulos contínuos.
**Técnicas:** análise discriminante, indução de regras, árvores de decisão, redes neurais, k-vizinhos mais próximos, raciocínio baseado em casos, algoritmos genéticos.
*Ex: classificar novos solicitantes de crédito como risco baixo ou alto a partir do comportamento de pagamento de clientes existentes.*

## 5. Predição
Muito parecida com classificação, mas o atributo-alvo é contínuo, não discreto. O objetivo é achar o valor numérico do alvo para objetos não vistos. Na literatura é às vezes chamada de regressão; com séries temporais, de previsão (forecasting).
**Técnicas:** análise de regressão, árvores de regressão, redes neurais, k-vizinhos, métodos Box-Jenkins, algoritmos genéticos.
*Ex: prever o faturamento anual da empresa a partir de gastos com publicidade, câmbio, inflação etc.*

## 6. Análise de dependência
Encontrar um modelo que descreva dependências (ou associações) significativas entre itens ou eventos. Usada sobretudo para entendimento, mas também para predição. Dependências podem ser estritas ou probabilísticas.
- **Associações** (caso especial popular): afinidades entre itens que ocorrem juntos com frequência. *Ex: "em 30% das compras, cerveja e amendoim foram levados juntos."* Algoritmos são rápidos e geram muitas associações — selecionar as interessantes é o desafio.
- **Padrões sequenciais:** dependências em que a ordem dos eventos importa (padrões de compra ao longo do tempo).
Frequentemente coocorre com segmentação (em dados grandes, dependências só ficam significativas em segmentos homogêneos).
**Técnicas:** análise de correlação, regressão, regras de associação, redes bayesianas, programação lógica indutiva, visualização.
*Ex: se um rádio é pedido, uma câmbio automático é pedido junto em 95% dos casos → ofertar como combo.*

---

**Dica de uso:** raramente um projeto é de um tipo só. Comece pela descrição/sumarização, use segmentação para tornar o problema tratável, e combine com classificação/predição/dependência conforme a meta de negócio.

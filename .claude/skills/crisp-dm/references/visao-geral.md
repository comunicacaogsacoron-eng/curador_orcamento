# Visão geral do processo CRISP-DM

Mapa completo: as seis fases, suas tarefas genéricas e os entregáveis de cada uma. Use para orientação e para responder "o que vem depois?".

## Fases × Tarefas × Entregáveis

### 1. Entendimento do Negócio
- **Determinar objetivos de negócio** → Contexto (background), Objetivos de negócio, Critérios de sucesso de negócio
- **Avaliar a situação** → Inventário de recursos, Requisitos/premissas/restrições, Riscos e contingências, Terminologia, Custos e benefícios
- **Determinar metas de mineração de dados** → Metas de dados, Critérios de sucesso de dados
- **Produzir plano do projeto** → Plano do projeto, Avaliação inicial de ferramentas e técnicas

### 2. Entendimento dos Dados
- **Coletar dados iniciais** → Relatório de coleta inicial
- **Descrever os dados** → Relatório de descrição dos dados
- **Explorar os dados** → Relatório de exploração dos dados
- **Verificar a qualidade dos dados** → Relatório de qualidade dos dados

### 3. Preparação dos Dados
- (saída geral da fase) → Dataset, Descrição do dataset
- **Selecionar dados** → Justificativa de inclusão/exclusão
- **Limpar dados** → Relatório de limpeza
- **Construir dados** → Atributos derivados, Registros gerados
- **Integrar dados** → Dados mesclados
- **Formatar dados** → Dados reformatados

### 4. Modelagem
- **Selecionar técnica de modelagem** → Técnica de modelagem, Premissas de modelagem
- **Gerar desenho de teste** → Desenho de teste
- **Construir modelo** → Configurações de parâmetros, Modelos, Descrição do modelo
- **Avaliar modelo** → Avaliação do modelo, Configurações revisadas de parâmetros

### 5. Avaliação
- **Avaliar resultados** → Avaliação dos resultados frente aos critérios de sucesso de negócio, Modelos aprovados
- **Revisar o processo** → Revisão do processo
- **Determinar próximos passos** → Lista de ações possíveis, Decisão

### 6. Implantação
- **Planejar implantação** → Plano de implantação
- **Planejar monitoramento e manutenção** → Plano de monitoramento e manutenção
- **Produzir relatório final** → Relatório final, Apresentação final
- **Revisar o projeto** → Documentação de experiência

## Dependências entre entregáveis (principais insumos)

Para produzir um entregável, estes são os principais insumos. Os objetivos de negócio são pervasivos — alimentam praticamente tudo.

- **Objetivos de negócio** ← Contexto
- **Critérios de sucesso de negócio** ← Objetivos de negócio
- **Requisitos/premissas/restrições** ← Objetivos de negócio
- **Riscos e contingências** ← Objetivos + Critérios de sucesso de negócio
- **Metas de dados** ← Objetivos de negócio + Requisitos/premissas/restrições
- **Critérios de sucesso de dados** ← Critérios de sucesso de negócio + Metas de dados
- **Plano do projeto** ← Objetivos + Inventário de recursos + Requisitos + Riscos
- **Relatório de coleta inicial** ← Metas de negócio + Inventário de recursos + Metas de dados
- **Relatório de descrição dos dados** ← Metas de negócio + Coleta inicial
- **Relatório de qualidade dos dados** ← Metas de negócio + Coleta inicial
- **Relatório de exploração** ← Metas de negócio + Descrição + Qualidade
- **Dataset e descrição** ← Metas de dados + Descrição + Qualidade + Exploração
- **Desenho de teste** ← Metas de dados + Critérios de sucesso de dados
- **Modelos** ← Metas de dados
- **Descrição do modelo** ← Modelos + Configurações de parâmetros + Desenho de teste
- **Avaliação do modelo** ← Critérios de sucesso de dados + Desenho de teste + Modelos
- **Avaliação frente ao negócio** ← Critérios de sucesso de negócio + Terminologia
- **Revisão do processo** ← Metas de negócio + Avaliação frente ao negócio
- **Próximos passos** ← Plano do projeto + Avaliação frente ao negócio
- **Plano de implantação** ← Metas de negócio + Requisitos/premissas/restrições
- **Plano de manutenção** ← Metas de negócio + Requisitos/premissas/restrições
- **Relatório/apresentação final** ← Metas de negócio + Terminologia + Avaliação frente ao negócio
- **Documentação de experiência** ← Plano do projeto + Revisão do processo

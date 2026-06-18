# Fase 5 — Avaliação

Você construiu modelos que parecem ter boa qualidade técnica. Antes de implantar, avalie de forma mais ampla: o modelo atende aos **objetivos de negócio**? Algum aspecto importante do negócio foi deixado de fora? Ao fim desta fase, decide-se sobre o uso dos resultados.

> Equação útil: **RESULTADOS = MODELOS + DESCOBERTAS.** A saída total do projeto não é só o modelo, mas também descobertas — qualquer coisa relevante para os objetivos do negócio ou que leve a novas perguntas (ex: problemas de qualidade de dados revelados pelo projeto).

Três tarefas: avaliar resultados → revisar o processo → determinar próximos passos.

---

## 5.1 Avaliar resultados

Avaliar o quanto o modelo atende aos objetivos de negócio (não só acurácia técnica) e se há razão de negócio para considerá-lo deficiente. Se tempo e orçamento permitirem, testar em aplicação real.

**Perguntas-chave:**
- O projeto atingiu os objetivos de negócio originais?
- O resultado é novo e útil frente ao conhecimento existente?
- Que descobertas (além dos modelos) emergiram? Geram novas perguntas?
- Surgiram novos objetivos de negócio para tratar depois?

**Entregáveis:**
- Avaliação dos resultados frente aos critérios de sucesso de negócio (com declaração final: o projeto já atende aos objetivos iniciais?)
- Modelos aprovados (os que atendem aos critérios)

---

## 5.2 Revisar o processo

Revisão de qualidade (QA) de todo o engajamento: algum fator ou tarefa importante foi negligenciado? O modelo foi construído corretamente? Só foram usados atributos permitidos e disponíveis para análises futuras?

**Perguntas-chave, para cada etapa do processo:**
- Era necessária, em retrospecto? Foi executada de forma ótima? Como poderia melhorar?
- Houve falhas, passos enganosos, caminhos inesperados?

**Entregável:** Revisão do processo — resumo, com atividades que faltaram e/ou deveriam ser repetidas.

---

## 5.3 Determinar próximos passos

Decidir como proceder: finalizar e ir para implantação, iniciar novas iterações, ou montar novos projetos. Considera recursos e orçamento remanescentes.

**Perguntas-chave:**
- Qual o potencial de implantação de cada resultado?
- Os recursos restantes permitem mais iterações?
- Quais as ações possíveis, com prós e contras de cada uma?

**Entregáveis:**
- Lista de ações possíveis (com razões a favor e contra)
- Decisão (a escolha, com a justificativa)

---

## Template de entregável — Avaliação

```markdown
# Avaliação — [Nome do Projeto]

## Avaliação dos resultados frente ao negócio
Para cada critério de sucesso de negócio:
- Comparação detalhada critério × resultado:
- O critério é atingível? O processo é adequado?
- Revisão do sucesso do projeto: atingiu os objetivos originais?
- Novos objetivos de negócio para depois?
- Conclusões para projetos futuros:

## Modelos aprovados
[Modelos que atendem aos critérios de sucesso de negócio]

## Revisão do processo
- Visão geral do processo usado:
- Por etapa: necessária? ótima? como melhorar?
- Falhas, passos enganosos, alternativas:

## Próximos passos
| Ação possível | A favor | Contra |
|---------------|---------|--------|

## Decisão
[Como proceder + justificativa]
```

**Próxima fase:** Implantação (`06-implantacao.md`) — se a decisão for seguir. Caso contrário, novas iterações ou novos projetos.

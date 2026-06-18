# Fase 6 — Implantação

Criar o modelo geralmente não é o fim. O conhecimento precisa ser organizado e apresentado de forma que o cliente consiga usar. Pode ir de gerar um relatório até implementar um processo repetível em toda a empresa. Muitas vezes é o cliente, não o analista, quem executa a implantação — então é importante que ele entenda de antemão o que precisa ser feito.

Quatro tarefas: planejar implantação → planejar monitoramento e manutenção → produzir relatório final → revisar o projeto.

---

## 6.1 Planejar implantação

A partir dos resultados da avaliação, concluir uma estratégia de implantação. Se houver um procedimento geral para gerar os modelos, documentá-lo aqui.

**Perguntas-chave:**
- Quais resultados são implantáveis?
- Como o conhecimento/informação será propagado aos usuários?
- Como cada modelo/software será implantado nos sistemas da organização?
- Como o uso será monitorado e os benefícios medidos?
- Que problemas podem surgir na implantação (armadilhas)?

**Entregável:** Plano de implantação — estratégia, passos necessários e como executá-los.

---

## 6.2 Planejar monitoramento e manutenção

Importante quando o resultado entra no dia a dia do negócio. Uma boa estratégia de manutenção evita longos períodos de uso incorreto dos resultados.

**Perguntas-chave:**
- Que aspectos dinâmicos podem mudar no ambiente?
- Como a acurácia será monitorada?
- Quando o modelo/resultado não deve mais ser usado? (critérios: validade, limiar de acurácia, dados novos, mudança no domínio) O que fazer então (atualizar, novo projeto)?
- Os objetivos de negócio do uso do modelo podem mudar com o tempo?

**Entregável:** Plano de monitoramento e manutenção.

---

## 6.3 Produzir relatório final

O líder e a equipe escrevem o relatório final. Pode ser um resumo do projeto e suas experiências, ou uma apresentação final e abrangente dos resultados — depende do plano de implantação e da audiência.

**Perguntas-chave:**
- Que relatórios são necessários (slides, sumário executivo, achados detalhados, explicação dos modelos)?
- Quão bem as metas de dados iniciais foram atingidas?
- Quem são os públicos-alvo? Que achados incluir para cada um?

**Entregáveis:**
- Relatório final (resultados, processo, custos, desvios do plano, planos de implementação, recomendações)
- Apresentação final (subconjunto do relatório, estruturado para a audiência — ex: patrocinador)

---

## 6.4 Revisar o projeto

Avaliar o que deu certo e o que deu errado, o que foi bem feito e o que precisa melhorar.

**Perguntas-chave:**
- O que dizem os envolvidos sobre suas experiências no projeto?
- Se há usuários finais usando o resultado: estão satisfeitos? O que poderia ser melhor?
- Que armadilhas, abordagens enganosas ou dicas valem registrar para projetos futuros?
- Como abstrair as lições para que sirvam a projetos comparáveis?

**Entregável:** Documentação de experiência.

---

## Template de entregável — Implantação

```markdown
# Implantação — [Nome do Projeto]

## Plano de implantação
- Resultados implantáveis:
- Estratégia e passos de implantação:
- Como o uso será monitorado / benefícios medidos:
- Armadilhas previstas:

## Plano de monitoramento e manutenção
Para cada resultado implantado:
- O que pode mudar no ambiente:
- Como a atualização será disparada (regular, evento, monitoramento):
- Como a atualização será feita:
- Quando parar de usar o resultado (critérios):

## Relatório final
- Resumo do Entendimento do Negócio (contexto, objetivos, critérios):
- Resumo do processo de dados:
- Resumo dos resultados:
- Resumo da avaliação:
- Resumo dos planos de implantação e manutenção:
- Análise custo/benefício:
- Conclusões para o negócio:
- Conclusões para projetos futuros:

## Apresentação final
[Subconjunto do relatório, estruturado para a audiência]

## Documentação de experiência
- Feedback dos envolvidos:
- O que funcionou bem / erros / lições:
- Dicas abstraídas para projetos futuros:
```

**Fim do ciclo — que é também um começo.** O resultado implantado e as lições aprendidas tendem a gerar novas perguntas de negócio, mais focadas. Projetos seguintes se beneficiam das experiências deste. Se novas perguntas surgirem, volte ao Entendimento do Negócio (`01-entendimento-negocio.md`).

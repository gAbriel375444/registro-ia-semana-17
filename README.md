Instanlando a biblioteca pandas com pip install pandas

Etapa 1 - Análise de Correlação

Ao analisar a matriz de correlação gerada a partir dos dados dos alunos, identificamos uma forte correlação linear positiva entre as variáveis horas_estudo e nota_anterior (com um valor de coeficiente de Pearson muito próximo de 1).O que isso significa na prática:Significa que, no comportamento desse grupo de alunos, existe uma tendência clara e previsível de que quanto maior o tempo dedicado às horas de estudo, maior tende a ser a nota anterior obtida pelo aluno.As demais variáveis (como exercicios, frequencia e participacao) apresentaram correlação próxima a 0 entre si e com as notas, o que indica que, neste conjunto de dados específico, elas se comportam de maneira independente e não possuem uma relação linear direta com o desempenho acadêmico medido.

Etapa 2 - Redução de colinearidade

A váriavel escolhida é a notas_anterior, pois é altamente correlacionada à horas_estudo (têm 0.90 de correlação). A recomendação é remover a var notas_anterior do conjunto de dados antes do treinamento do modelo. A colinearidade extrema gera redundância, overfitting e a instabilidade do modelo.

Etapa 3 — Criação de nova feature


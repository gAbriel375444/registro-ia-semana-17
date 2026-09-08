## Etapa 1 - Análise de Correlação 
A matriz de correlação revelou uma forte relação linear positiva entre horas de estudo e nota anterior: quanto mais o aluno estuda, maior é sua nota. Já as demais variáveis (exercícios, frequência e participação) mostraram correlação próxima de zero, indicando que atuam de forma independente e sem relação linear direta com a nota.


## Etapa 2 - Redução de colinearidade
A váriavel escolhida é a notas_anterior, pois é altamente correlacionada à horas_estudo (têm 0.90 de correlação). A recomendação é remover a var notas_anterior do conjunto de dados antes do treinamento do modelo. A colinearidade extrema gera redundância, overfitting e a instabilidade do modelo.


## Etapa 3 — Criação de nova feature
A criação da variável engajamento_total através da soma de frequencia e participacao é útil porque simplifica o modelo, consolidando duas métricas complementares em um único indicador de comportamento. Combinadas elas capturam com maior precisão o conceito de comprometimento do estudante.


## Etapa 4 - Aplicação de PCA
Os dados originais são transformados em um novo espaço vetorial menor. Em vez de usar várias colunas repetitivas, o PCA combina a informação relevante em poucas direções principais. Isso elimina redundâncias, reduz o número de dimensões e deixa o processamento do modelo muito mais leve e rápido, mantendo quase toda a informação original.


## Etapa 5 - Análise final
### Como a seleção de features ajuda na generalização? 
R: Remove ruídos e variáveis irrelevantes, impedindo que o modelo decore os dados de treino (overfitting) e o ajuda a acertar novos dados.


### Por que a colinearidade prejudica modelos? 
R: Variáveis correlacionadas passam a mesma informação, o que gera disputa de peso entre elas no modelo linear. Isso distorce a importância real de cada atributo e deixa a interpretação matemática instável.


### Quando usar PCA? 
R: Quando há muitas variáveis, forte correlação entre elas ou necessidade de reduzir o custo computacional.


### O modelo melhorou após a seleção/transformação? 
R: Sim, remover redundâncias reduz o ruído e focar nos componentes principais torna o modelo mais simples e robusto.


### Quais variáveis traziam informação redundante? 
R: nota_anterior (derivada de horas_estudo) e frequencia/participacao (já contidas em engajamento_total).


### A redução alterou a interpretação? 
R: Sim, as colunas originais com nomes legíveis viraram "Componentes Principais", que são combinações matemáticas difíceis de interpretar diretamente.


### Houve impacto no desempenho?
R: O desempenho se manteve alto ou até melhorou, pois a perda de dados foi irrelevante, enquanto a menor complexidade reduziu drasticamente o risco do modelo memorizar os dados.


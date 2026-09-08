# importando as bibliotecas numpy
# e pandas e dando um apelido para elas
import pandas as pd
import numpy as np

# definindo uma seed para o numpy
# garanto que em todas as 'rodadas'
# os mesmos resultados serão apresentados 
np.random.seed(42)

# criando uma tabela
dados = pd.DataFrame({
    "horas_estudo": np.random.randint(1, 6, 50),
    "exercicios": np.random.randint(10, 100, 50),
    "frequencia": np.random.randint(60, 100, 50),
    "participacao": np.random.randint(1, 10, 50),
})

# adiciona mais uma coluna à tabela "nota_anterior"
# pega as horas de estudo e múltiplica por 1.5
# e depois soma com um número aleatório entre 0 e 1 (assim nem todo mundo que estudou 4h fica com 6, por exemplo,
# ficam 6.3 ou 6.5...)
dados["nota_anterior"] = dados["horas_estudo"] * 1.5 + np.random.normal(0, 1, 50)

# exibe a tabela
print(dados)

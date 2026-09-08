# importando as bibliotecas numpy
# e pandas e dando um apelido para elas
import pandas as pd
import numpy as np

np.random.seed(42)

dados = pd.DataFrame({
    "horas_estudo": np.random.randint(1, 6, 50),
    "exercicios": np.random.randint(10, 100, 50),
    "frequencia": np.random.randint(60, 100, 50),
    "participacao": np.random.randint(1, 10, 50),
})

dados["nota_anterior"] = dados["horas_estudo"] * 1.5 + np.random.normal(0, 1, 50)

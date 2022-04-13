""" Case of use of Apriory algorithm"""

import pandas as pd
from classes.apyori import apriori

dados = pd.read_csv('brindes.csv', header=None)
transacoes = []
for i in range(0, dados.shape[0]):
    transacoes.append(
        [str(dados.values[i, j]) for j in range(0, dados.shape[1])]
    )

regras = apriori(
    transacoes,
    min_support=0.1,
    min_confidence=0.05,
    min_lift=2,
    # min_lenght=2
)

resultados = list(regras)

resultados2 = [list(x) for x in resultados]

resultadoFormatado = []
for j in range(0, len(resultados2)):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])
print(resultadoFormatado)

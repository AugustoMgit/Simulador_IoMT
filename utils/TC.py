import random
import numpy as np

def TC(qtValores, minMinutos, MaxMinutos):
    normais = int((qtValores * 80) / 100)
    anormais = int((qtValores * 20) / 100)

    # Gerando os valores normais
    valoresNormais = np.random.uniform(36, 37.5, normais)

    # Gerando os valores anormais
    valoresAnormais1 = np.random.uniform(30, 36, int(anormais / 2))
    valoresAnormais2 = np.random.uniform(37.6, 45, int(anormais / 2))
    valoresAnormais = np.concatenate((valoresAnormais1, valoresAnormais2))

    print(valoresAnormais)


TC(40, 0, 60)

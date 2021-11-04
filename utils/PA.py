import numpy as np

def PA(qtValores, minMinutos, MaxMinutos):
    normais = int(qtValores * 0.8)
    anormais = int(qtValores * 0.2)

    # Gerando os valores normais
    sistolicaNormal = np.random.randint(110, 129, normais)
    diastolicaNormal = np.random.randint(70, 84, normais)
    print(sistolicaNormal, diastolicaNormal)

    # Gerando os valores anormais
    sistolicaAnormais = np.random.randint(0, 109, anormais)
    diastolicaAnormais = np.random.randint(0, 69, anormais)
    print(sistolicaAnormais, diastolicaAnormais)


PA(80, 30, 120)
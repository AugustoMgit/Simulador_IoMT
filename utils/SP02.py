import numpy as np

def FrequenciaCardiaca(qtValores):
    normais = int(qtValores * 0.8)
    anormais = int(qtValores * 0.2)

    # Gerando os valores normais
    valoresNormais = np.random.uniform(50, 100, normais)

    # Gerando os valores anormais
    valoresAnormais1 = np.random.uniform(0, 49, int(anormais / 2))
    valoresAnormais2 = np.random.uniform(101, 200, int(anormais / 2))
    valoresAnormais = np.concatenate((valoresAnormais1, valoresAnormais2))

    return(valoresNormais, valoresAnormais)


def SP02(qtValores, minMinutos, MaxMinutos):
    normais = int(qtValores * 0.8)
    anormais = int(qtValores * 0.2)

    # Gerando os valores normais
    valoresNormais = np.random.uniform(90, 100, normais)

    # Gerando os valores anormais
    valoresAnormais1 = np.random.uniform(50, 89, int(anormais / 2))
    valoresAnormais2 = np.random.uniform(0, 50, int(anormais / 2))
    valoresAnormais = np.concatenate((valoresAnormais1, valoresAnormais2))

    frequenciaCardiaca = FrequenciaCardiaca(qtValores)
    frequenciaCardiacaNormais = frequenciaCardiaca[0]
    frequenciaCardiacaAnormais = frequenciaCardiaca[1]


#SP02(40, 0, 60)

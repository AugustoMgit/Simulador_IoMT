import numpy as np
import random
from datetime import datetime, timedelta, time
import matplotlib.pyplot as plt
import pandas as pd

def PA(qtValores, minMinutos, MaxMinutos):
    normais = int(qtValores * 0.8)
    anormais = int(qtValores * 0.2)

    minutes = 0
    today = datetime.today()
    date = datetime(today.year, today.month, today.day, 8, 30, 0)

    # Gerando os valores normais
    sistolicaNormal = np.random.randint(110, 129, normais)
    diastolicaNormal = np.random.randint(70, 84, normais)
    pressaoNormal = np.concatenate((sistolicaNormal, diastolicaNormal))

    # Gerando os valores anormais
    sistolicaAnormais1 = np.random.randint(0, 109, int(anormais / 2))
    sistolicaAnormais2 = np.random.randint(130, 300, int(anormais / 2))
    sistolicaAnormais = np.concatenate((sistolicaAnormais1, sistolicaAnormais2))

    diastolicaAnormais1 = np.random.randint(0, 69, int(anormais / 2))
    diastolicaAnormais2 = np.random.randint(85, 300, int(anormais / 2))
    diastolicaAnormais = np.concatenate((diastolicaAnormais1, diastolicaAnormais2))

    pressaoAnormal = np.concatenate((sistolicaAnormais, diastolicaAnormais))

    # Gerando os valores de PA
    valores = np.concatenate((pressaoNormal, pressaoAnormal))
    np.random.shuffle(valores)

    dataPlot = []
    for i in range(len(valores)):
        valores[i] = round(valores[i], 2)
        minutes +=random.randint(minMinutos, MaxMinutos)
        delta = timedelta(minutes=minutes)
        dateTime = (date + delta)
        dataPlot.append(tuple([dateTime, valores[i]]))

    df = pd.DataFrame(dataPlot, columns=['Data', 'PA'])
    plt.plot(df['Data'], df['PA'])
    plt.ylabel("%")
    plt.xlabel("Hora")
    plt.legend()
    plt.savefig('../images/plots/PA.png')


PA(20, 30, 120)
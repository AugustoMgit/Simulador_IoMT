import numpy as np
import random
from datetime import datetime, timedelta, time

def TemperaturaCorporal(qtValores, minMinutos, MaxMinutos):
    normais = int(qtValores * 0.8)
    anormais = int(qtValores * 0.2)

    minutes = 0
    today = datetime.today()
    date = datetime(today.year, today.month, today.day, 8, 30, 0)

    # Gerando os valores normais
    valoresNormais = np.random.uniform(36, 37.5, normais)

    # Gerando os valores anormais
    valoresAnormais1 = np.random.uniform(30, 36, int(anormais / 2))
    valoresAnormais2 = np.random.uniform(37.6, 45, int(anormais / 2))
    valoresAnormais = np.concatenate((valoresAnormais1, valoresAnormais2))

    for i in range(len(valoresNormais)):
        valoresNormais[i] = round(valoresNormais[i], 2)
        minutes +=random.randint(minMinutos, MaxMinutos)
        delta = timedelta(minutes=minutes)
        dateTime = (date + delta)

        print(dateTime)

    print("\n")
    date = datetime(today.year, today.month, today.day, 13, 30, 0)
    minutes = 0
    for i in range(len(valoresAnormais)):
        valoresAnormais[i] = round(valoresAnormais[i], 2)
        minutes +=random.randint(minMinutos, MaxMinutos)
        delta = timedelta(minutes=minutes)
        dateTime = (date + delta)
        print(dateTime)


TemperaturaCorporal(20, 5, 60)

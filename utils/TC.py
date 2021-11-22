import numpy as np
import random
from datetime import datetime, timedelta, time

def TemperaturaCorporal(qtValores, minMinutos, MaxMinutos):
    normais = int(qtValores * 0.8)
    anormais = int(qtValores * 0.2)

    minutes = 0
    today = datetime.today()
    date = datetime(today.year, today.month, today.day, random.randint(6, 10), random.randint(0, 59), 0)

    # Gerando os valores normais
    valoresNormais = np.random.uniform(36, 37.5, normais)

    # Gerando os valores anormais
    valoresAnormais1 = np.random.uniform(30, 36, int(anormais / 2))
    valoresAnormais2 = np.random.uniform(37.6, 45, int(anormais / 2))
    valoresAnormais = np.concatenate((valoresAnormais1, valoresAnormais2))

    valores = np.concatenate((valoresNormais, valoresAnormais))
    np.random.shuffle(valores)

    for i in range(len(valores)):
        valores[i] = round(valores[i], 2)
        minutes += random.randint(minMinutos, MaxMinutos)
        delta = timedelta(minutes=minutes)
        dateTime = (date + delta)

        dataPlot.append(tuple((dateTime, valores[i])))

        ### Chamar WS-Rest
        dados = {
            "id_user": 1,
            "data": dateTime.strftime("%Y-%m-%d %H:%M:%S"),
            "valor1": valores[i],
            "valor2": None,
            "tipo": "TC"
        }

        response = requests.put(URL_BASE + "/add", data=dados)
        if (response.status_code != 200)
            return 'Ocorreu um erro!'


#TemperaturaCorporal(20, 5, 60)

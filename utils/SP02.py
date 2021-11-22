import numpy as np
import random
from datetime import datetime, timedelta, time

URL_BASE = "http://localhost:5000/api"

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

    minutes = 0
    today = datetime.today()

    date = datetime(today.year, today.month, today.day, random.randint(6, 10), random.randint(0, 59), 0)

    # Gerando os valores normais
    valoresNormais = np.random.uniform(90, 100, normais)

    # Gerando os valores anormais
    valoresAnormais1 = np.random.uniform(50, 89, int(anormais / 2))
    valoresAnormais2 = np.random.uniform(0, 50, int(anormais / 2))
    valoresAnormais = np.concatenate((valoresAnormais1, valoresAnormais2))

    frequenciaCardiaca = FrequenciaCardiaca(qtValores)
    frequenciaCardiaca = np.concatenate((frequenciaCardiaca[0], frequenciaCardiaca[1]))

    # Gerando os valores de SP02
    valores = np.concatenate((valoresNormais, valoresAnormais))
    np.random.shuffle(valores)

    for i in range(len(valores)):
        valores[i] = round(valores[i], 2)
        frequenciaCardiaca[i] = round(frequenciaCardiaca[i], 2)
        minutes +=random.randint(minMinutos, MaxMinutos)
        delta = timedelta(minutes=minutes)
        dateTime = (date + delta)

        # chamar ws-rest
        dados = {
                  "id_user": 1,
                  "data": dateTime.strftime("%Y-%m-%d %H:%M:%S"),
                  "valor1": valores[i],
                  "valor2": frequenciaCardiaca[i],
                  "tipo": "SP02"
                }

        response = requests.put(URL_BASE + "/add", data=dados)
        if (response.status_code != 200)
            return 'Ocorreu um erro!'


#SP02(20, 5, 60)

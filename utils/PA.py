import numpy as np
import random
from datetime import datetime, timedelta, time
import pandas as pd
import json, requests
URL_BASE = "http://localhost:5000/api"

def PA(qtValores, minMinutos, MaxMinutos):
    normais = int(qtValores * 0.8)
    anormais = int(qtValores * 0.2)

    minutes = 0
    today = datetime.today()
    date = datetime(today.year, today.month, today.day, random.randint(6, 10), random.randint(0, 59), 0)

    # Gerando os valores normais
    sistolicaNormal = np.random.randint(110, 129, normais)
    diastolicaNormal = np.random.randint(70, 84, normais)
    pressaoNormal = pd.DataFrame({"Sistolica": sistolicaNormal, "Diastolica": diastolicaNormal})

    # Gerando os valores anormais
    sistolicaAnormais1 = np.random.randint(0, 109, int(anormais / 2))
    sistolicaAnormais2 = np.random.randint(130, 300, int(anormais / 2))
    sistolicaAnormais = np.concatenate((sistolicaAnormais1, sistolicaAnormais2))

    diastolicaAnormais1 = np.random.randint(0, 69, int(anormais / 2))
    diastolicaAnormais2 = np.random.randint(85, 300, int(anormais / 2))
    diastolicaAnormais = np.concatenate((diastolicaAnormais1, diastolicaAnormais2))

    pressaoAnormal = pd.DataFrame({"Sistolica": sistolicaAnormais, "Diastolica": diastolicaAnormais})

    # Gerando os valores de PA
    valores = pd.concat([pressaoNormal, pressaoAnormal])
    valores = valores.sample(frac=1).reset_index(drop=True)

    for i in range(len(valores)):
        minutes += random.randint(minMinutos, MaxMinutos)
        delta = timedelta(minutes=minutes)
        dateTime = (date + delta)

        # chamar ws-rest
        dados =  {
                  "id_user": 1,
                  "data": dateTime.strftime("%Y-%m-%d %H:%M:%S"),
                  "valor1": valores.iloc[i]["Sistolica"],
                  "valor2": valores.iloc[i]["Diastolica"],
                  "tipo": "PA"
                }

        response = requests.put(URL_BASE + "/add", data=dados)
        if (response.status_code != 200):
            return 'Ocorreu um erro!'

    return ('Dados inseridos com sucesso!')

PA(20, 30, 120)

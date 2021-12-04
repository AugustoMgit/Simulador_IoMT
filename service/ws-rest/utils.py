import numpy as np
import random
from datetime import datetime, timedelta, time
import pandas as pd
import json, requests

URL_BASE = "http://localhost:5000/api"

def PA(id_user, qtValores, minMinutos, MaxMinutos):
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


def SP02(id_user, qtValores, minMinutos, MaxMinutos):
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
        if (response.status_code != 200):
            return 'Ocorreu um erro!'

    return ('Dados inseridos com sucesso!')


def TemperaturaCorporal(id_user, qtValores, minMinutos, MaxMinutos):
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

        ### Chamar WS-Rest
        dados = {
            "id_user": id_user,
            "data": dateTime.strftime("%Y-%m-%d %H:%M:%S"),
            "valor1": valores[i],
            "valor2": None,
            "tipo": "TC"
        }

        response = requests.put(URL_BASE + "/add", data=dados)
        if (response.status_code != 200):
            return 'Ocorreu um erro!'

    return ('Dados inseridos com sucesso!')

def verificarSituacoesEspecificas1(id_user):
    # Verificar se existe alguma situação especifica
    msg = ""
    response = requests.get(URL_BASE + "/dadosSituacao1/" + str(id_user))
    if (response.status_code != 200):
        return 'Ocorreu um erro!'

    situacoesEspecificas = json.loads(response.text)

    ### chamar end point para enviar email...
    if (situacoesEspecificas['len'] > 0):
        msg = 'Atenção!!! Sua temperatura corporal mudou brutamente em um intervalo de tempo! Entre em contato com um médico!!'
    else:
        msg = 'Sua Temperatura Corporal está normal! Parabéns!'

    dados = {
        'id_user': id_user,
        'msg': msg
    }

    response = requests.post(URL_BASE + "/emailsituacoesEspecificas", data=dados)
    if (response.status_code != 200):
        print (response.text)


def verificarSituacoesEspecificas2(id_user):
    # Verificar se existe alguma situação especifica
    msg = ""
    response = requests.get(URL_BASE + "/dadosSituacao2/" + str(id_user))
    if (response.status_code != 200):
        return 'Ocorreu um erro!'

    situacoesEspecificas = json.loads(response.text)
    dados = situacoesEspecificas['Data']
    diastolica = []
    sistolica = []

    for d in dados:
        diastolica.append(float(d['diastolica']))
        sistolica.append(float(d['sistolica']))
    
    ### chamar end point para enviar email...
    if (abs(diastolica[0] - diastolica[1]) > 10 and abs(diastolica[1] - diastolica[2]) > 10):
        msg = 'Atenção!!! Sua pressão arterial diastolica mudou brutamente em um intervalo de tempo! Entre em contato com um médico!!'

    if (abs(sistolica[0] - sistolica[1]) > 10 and abs(sistolica[1] - sistolica[2]) > 10):
        msg = 'Atenção!!! Sua pressão arterial sistolica mudou brutamente em um intervalo de tempo! Entre em contato com um médico!!'

    if (msg != ""):
        dados = {
            "id_user": id_user,
            "msg": msg
        }

        response = requests.post(URL_BASE + "/emailsituacoesEspecificas", data=dados)
        if (response.status_code != 200):
            return 'Ocorreu um erro!'


def verificarSituacoesEspecificas(id_user):
    verificarSituacoesEspecificas1(id_user)
    #verificarSituacoesEspecificas2(id_user)



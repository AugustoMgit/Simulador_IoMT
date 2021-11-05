import numpy as np
import random
from datetime import datetime, timedelta, time
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector

def PA(qtValores, minMinutos, MaxMinutos):
    database = mysql.connector.connect(host="localhost", user="root", password="", database = "iomt")
    sql = "INSERT INTO dadoscoletados (usuario, valor1, valor2, dataHora, tipo) VALUES (%s, %s, %s, %s, %s)"

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

    dataPlot = []
    for i in range(len(valores)):
        minutes += random.randint(minMinutos, MaxMinutos)
        delta = timedelta(minutes=minutes)
        dateTime = (date + delta)
        dataPlot.append(tuple([dateTime, valores.Sistolica[i], valores.Diastolica[i]]))

        cursor = database.cursor()
        val = (3, int(valores.Sistolica[i]), int(valores.Diastolica[i]), datetime.strftime(dateTime, '%Y-%m-%d %H:%M:%S'), "PA")
        cursor.execute(sql, val)

        database.commit()
        cursor.close()

    database.close()

    df = pd.DataFrame(dataPlot, columns=['Data', 'Sistolica', 'Diastolica'])
    plt.plot(df['Data'], df['Sistolica'], 'r-', label='Sistolica', color = 'red')
    plt.plot(df['Data'], df['Diastolica'], 'r-', label='Diastolica', color = 'blue')
    plt.xlabel("Hora")
    plt.legend()
    plt.savefig('../images/plots/PA.png')


PA(20, 30, 120)

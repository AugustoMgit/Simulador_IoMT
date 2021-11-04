import numpy as np
import random
from datetime import datetime, timedelta, time
import matplotlib.pyplot as plt
import mysql.connector

def TemperaturaCorporal(qtValores, minMinutos, MaxMinutos):
    database = mysql.connector.connect(host="localhost", user="root", password="", database = "iomt")
    sql = "INSERT INTO dadoscoletados (usuario, valor1, valor2, dataHora, tipo) VALUES (%s, %s, %s, %s, %s)"
    normais = int(qtValores * 0.8)
    anormais = int(qtValores * 0.2)

    minutes = 0
    today = datetime.today()
    mes = random.randint(1, 12)
    dia = random.randint(1, 30)

    if (mes == 2 and dia >= 28):
        dia = 28

    date = datetime(today.year, mes, dia, random.randint(6, 10), random.randint(0, 59), 0)

    # Gerando os valores normais
    valoresNormais = np.random.uniform(36, 37.5, normais)

    # Gerando os valores anormais
    valoresAnormais1 = np.random.uniform(30, 36, int(anormais / 2))
    valoresAnormais2 = np.random.uniform(37.6, 45, int(anormais / 2))
    valoresAnormais = np.concatenate((valoresAnormais1, valoresAnormais2))

    valores = np.concatenate((valoresNormais, valoresAnormais))
    np.random.shuffle(valores)
    dataPlot = []

    for i in range(len(valores)):
        valores[i] = round(valores[i], 2)
        minutes += random.randint(minMinutos, MaxMinutos)
        delta = timedelta(minutes=minutes)
        dateTime = (date + delta)

        dataPlot.append(tuple((dateTime, valores[i])))

        ### Chamar WS-Rest e salvar no banco de dados
        cursor = database.cursor()
        val = (4, valores[i], None, dateTime, "TC")
        cursor.execute(sql, val)

        database.commit()
        cursor.close()

    database.close()

    plt.plot(*zip(*dataPlot))
    plt.title("Temperatura Corporal " + datetime.today().strftime('%Y-%m-%d'))
    plt.ylabel("°C")
    plt.xlabel("Hora")
    plt.legend(["Temperatura Corporal"])
    plt.savefig('../images/plots/TC.png')


TemperaturaCorporal(20, 5, 60)

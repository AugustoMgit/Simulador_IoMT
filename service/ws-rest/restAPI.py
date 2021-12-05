import json
import pymysql
from flask import request, jsonify
import flask
import datetime
from flask import Flask
from flask_cors import CORS
import utils
import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

class BD(object):
    
    def verifyUserExists(self, id_user):
        conn_ver = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_ver = conn_ver.cursor()
        sql = "select id FROM usuario WHERE id = %s"
        data = (id_user)
        cursor_ver.execute(sql, data)
        if cursor_ver.rowcount==0:
            cursor_ver.close()
            conn_ver.close()
            return 0
        else:
            cursor_ver.close()
            conn_ver.close()
            return 1
        
    def verifyDados(self, id_dado):
        conn_ver = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_ver = conn_ver.cursor()
        sql = "select id FROM DadosColetados WHERE id = %s"
        data = (id_dado)
        cursor_ver.execute(sql, data)
        if cursor_ver.rowcount==0:
            cursor_ver.close()
            conn_ver.close()
            return 0
        else:
            cursor_ver.close()
            conn_ver.close()
            return 1

    def returnEmailUser(self, id_user):
        conn_ver = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_ver = conn_ver.cursor()
        sql = "select email FROM usuario WHERE id = %s"
        data = (id_user)
        cursor_ver.execute(sql, data)
        email_ser_check = cursor_ver.fetchall()[0][0]
        cursor_ver.close()
        conn_ver.close()
        return email_ser_check


    def addDados(self, id_user, value1, value2, type_, dataHora):
        if self.verifyUserExists(id_user) == 0: return {"ERROR": 'Usuario nao cadastrado'}
        conexao = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_add = conexao.cursor()
        sql = "INSERT INTO DadosColetados (usuario, valor1, valor2, dataHora, tipo) VALUES (%s,%s,%s,%s,%s)"
        data = (id_user, value1, value2, dataHora, type_)
        cursor_add.execute(sql, data)
        conexao.commit()
        cursor_add.close()
        conexao.close()
        return {"ERROR":"", "Status":1}

    def changeDados(self, id_user, id_dado, valor1='', valor2='', tipo=''):
        if self.verifyUserExists(id_user) == 0: return {"ERROR": 'Usuario nao cadastrado'}
        if self.verifyDados(id_dado) == 0: return {"ERROR": 'Dado nao cadastrado'}

        connection = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor = connection.cursor()
        data = ()
        sql_parcial = "UPDATE DadosColetados SET"

        if valor1 != '':
            sql_parcial +=  " valor1 = %s" 
            data = data + (valor1,)
        if valor2 != '':
            if 'valor1' in sql_parcial:sql_parcial +=','
            sql_parcial += " valor2 = %s"
            data = data + (valor2,)
        if tipo != '':
            if 'valor1' in sql_parcial or 'valor2' in sql_parcial:sql_parcial +=','
            sql_parcial += " tipo = %s"
            data = data + (tipo,)
        sql_completo = sql_parcial + ' WHERE id = %s'

        data = data + (str(id_dado),)
        cursor.execute(sql_completo, data)
        connection.commit()
        cursor.close()
        connection.close()

        return {"ERROR":"", "Status":1}

    def getAllDados(self):
        conexao_getall = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_getall = conexao_getall.cursor()
        sql = "SELECT * FROM DadosColetados"
        cursor_getall.execute(sql)
        results_all = cursor_getall.fetchall()
        cursor_getall.close()
        conexao_getall.close()
        return results_all

    def getMyAllDados(self, id_user):
        if self.verifyUserExists(id_user) == 0: return -1
        conexao_getall = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_getall = conexao_getall.cursor()
        sql = "SELECT * FROM DadosColetados WHERE usuario = %s"
        cursor_getall.execute(sql, (id_user))
        results_all = cursor_getall.fetchall()
        cursor_getall.close()
        conexao_getall.close()
        return results_all
    
    def getMyDadoSpecify(self, id_user, id_dado):
        if self.verifyUserExists(id_user) == 0:return -1
        if self.verifyDados(id_dado) == 0:return -2
        conexao_getall = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_getall = conexao_getall.cursor()
        sql = "SELECT * FROM DadosColetados WHERE usuario = %s and id = %s"
        cursor_getall.execute(sql, (id_user,id_dado))
        results_all = cursor_getall.fetchall()
        cursor_getall.close()
        conexao_getall.close()
        return results_all

    def deleteDado(self, id_user, id_dado):
        if self.verifyUserExists(id_user) == 0:return {"ERROR":"Usuario nao existe", "Status":0}
        #if self.verifyDados(id_dado) == 0:return {"ERROR":"Dado nao existe", "Status":0}
        conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor = conn.cursor()
        sql = "DELETE FROM DadosColetados WHERE id = %s AND usuario = %s"
        sql_ver = "SELECT * FROM DadosColetados WHERE id = %s AND usuario = %s"
        data = (id_dado, id_user)
        cursor.execute(sql_ver, data)
        results_ver = cursor.fetchall()
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()
        if len(results_ver) == 0: return {"ERROR":"Dado nao existe", "Status":0}
        return {"ERROR":"", "Status":1}
    
    def deleteAllMyDados(self, id_user):
        if self.verifyUserExists(id_user) == 0:return {"ERROR":"Usuario nao existe", "Status":0}
        conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor = conn.cursor()
        sql = "DELETE FROM DadosColetados WHERE usuario = %s"
        data = (id_user)
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()
        return {"ERROR":"", "Status":1}

    def getDadosSituacaoEspecifica1(self, id_user):
        if self.verifyUserExists(id_user) == 0:return {"ERROR":"Usuario nao existe", "Status":0}
        conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor = conn.cursor()
        sql = "SELECT dc.usuario, dc.valor1 AS 'temperaturaCorporal', sub.valor1 AS 'SP02', sub.dataHora, dc.dataHora, ABS(TIMESTAMPDIFF(MINUTE , dc.dataHora , sub.dataHora)) AS diffHoras\n"
        sql += "FROM DadosColetados AS dc\n"
        sql += " JOIN (SELECT dc1.* FROM DadosColetados dc1 WHERE dc1.usuario = %s AND dc1.tipo = 'SP02' AND dc1.valor1 < 90 ) AS sub ON sub.usuario = dc.usuario\n"
        sql += "WHERE dc.usuario = %s AND dc.tipo = 'TC' AND dc.valor1 NOT BETWEEN 35 AND 37.5 HAVING ABS(TIMESTAMPDIFF(MINUTE , dc.dataHora , sub.dataHora)) < 60"
        data = (id_user, id_user)
        cursor.execute(sql, data)
        results_all = cursor.fetchall()
        cursor.close()
        conn.close()
        return results_all

    def getDadosSituacaoEspecifica2(self, id_user):
        if self.verifyUserExists(id_user) == 0:return {"ERROR":"Usuario nao existe", "Status":0}
        conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor = conn.cursor()
        sql = "SELECT d.usuario, d.valor1 AS sistolica, d.valor2 AS diastolica, d.dataHora FROM dadoscoletados d WHERE d.tipo = 'PA' AND d.usuario = %s AND dataHora BETWEEN date_sub(current_timestamp(), INTERVAL 24 HOUR) AND current_timestamp() ORDER BY dataHora DESC LIMIT 3"
        data = (id_user)
        cursor.execute(sql, data)
        results_all = cursor.fetchall()
        cursor.close()
        cursor.close()
        conn.close()
        return results_all


def sendEmailUserWarning(email_user, message):
    host = 'smtp.gmail.com'
    port = 587
    user = 'trabalhoSDupf2021@gmail.com'
    password = 'enviaremail'

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(user, password)

    email_msg = MIMEMultipart()
    email_msg['From'] = 'IOMT'
    email_msg['To'] = email_user
    email_msg['Subject'] = 'Situacao especifica'
    email_msg.attach(MIMEText(message, 'plain'))

    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    server.quit()

c = BD()

@app.route('/api/add', methods=['PUT', 'POST'])
def insertDados():
    request_data = request.get_json()
    user = request_data['id_user']
    
    if user == None or user == '': return jsonify({"ERROR":"ID usuario invalido", "Status":0})
    valor1 = request_data['valor1']
    s_error = ''
    if valor1 == '' or valor1 == None:
        s_error += 'Insira o valor 1. '

    valor2 = request_data['valor2']
    if valor2 == '' or valor2 == None:
        valor2 = None

    tipo = request_data['tipo']
    if tipo == '' or tipo == None:
        s_error +='Insira o tipo.'

    dataHora = datetime.datetime.now()
    if 'dataHora' in request_data:
        dataHora = request_data['data']

    if len(s_error) > 1:
        return jsonify({"ERROR":s_error.strip(), "Status":0})

    r = c.addDados(user, valor1, valor2, tipo, dataHora)

    return jsonify(r)

@app.route('/api/addsimulador', methods=['PUT', 'POST'])
def insertDadosSimualdor():
    user = request.form.get('id_user')
    
    if user == None or user == '': return jsonify({"ERROR":"ID usuario invalido", "Status":0})
    valor1 = request.form.get( 'valor1')
    s_error = ''
    if valor1 == '' or valor1 == None:
        s_error += 'Insira o valor 1. '

    valor2 = request.form.get( 'valor2')
    if valor2 == '' or valor2 == None:
        valor2 = None

    tipo = request.form.get('tipo')
    if tipo == '' or tipo == None:
        s_error +='Insira o tipo.'
    
    dataHora = request.form.get('data')

    if len(s_error) > 1:
        return jsonify({"ERROR":s_error.strip(), "Status":0})

    r = c.addDados(user, valor1, valor2, tipo, dataHora)

    return jsonify(r)

@app.route('/api/change/mydados', methods=['POST'])
def changeMyDados():
    request_data = request.get_json()

    id_dado = request_data['id_dado']
    id_user = request_data['id_user']
    valor1 = request_data['valor1']
    valor2 = request_data['valor2']
    tipo = request_data['tipo']
    
    valor1 = valor1 if valor1 != None else ''
    valor2 = valor2 if valor2 != None else ''
    tipo = tipo if tipo != None else ''

    if id_user == None: return jsonify({"ERROR":'ERROR ID USER'})
    if id_dado == None: return jsonify({"ERROR":'ERROR ID DADO'})

    if valor1 == ''and valor2 == '' and tipo == '':
        return jsonify({"ERROR":'Nenhum dado a ser alterado', 'Status':0})

    r = c.changeDados(id_user, id_dado, valor1, valor2, tipo)

    return jsonify(r)


#http://127.0.0.1:5000/api/get/mydado?iduser=1&iddado=2
@app.route('/api/get/mydado/<id_user>/<id_dado>', methods=['GET'])
def getDadosUnique(id_user, id_dado):
    id_user_get = id_user
    id_dado_get = id_dado

    if (id_user_get == '' or id_user_get == None) and (id_dado_get == '' or id_dado_get == None): 
        return jsonify({"ERROR": "ID usuario e ID dado invalido"})

    try: 
        int(id_user_get)
    except:
        return jsonify({"ERROR": "ID usuario invalido"})

    try:
        int(id_dado_get)    
    except:
        return jsonify({"ERROR": "ID dado invalido"})

    if id_user_get == '': 
        return jsonify({"ERROR": "ID usuario invalido"})
    if id_dado_get == '': 
        return jsonify({"ERROR": "ID dado invalido"})

    tup = c.getMyDadoSpecify(id_user_get, id_dado_get)

    if tup ==  -1 or tup ==  -2: 
        return jsonify({"ERROR": 'Nenhum dado encontrado', 'Status':0})

    list_json = []
    for t in tup:
        list_json.append({'valor1':t[2], 'valor2':t[3],'data':t[4], 'tipo':t[5]})

    return jsonify({"ERROR":"", "Data":list_json})


@app.route('/api/emailsituacoesEspecificas', methods=['POST'])
def mandaremailsituacoesEspecificas():
    user = request.form.get('id_user')
    message_send_email = request.form.get('msg')
    if message_send_email == None: return jsonify({"ERROR": 'mensagem sem conteudo'})
 
    email_user = c.returnEmailUser(id_user)
    if email_user != None:
        try:
            sendEmailUserWarning(email_user, message_send_email)
        except:
            return jsonify({"ERROR":"Erro ao enviar o email"})

        return jsonify({"ERROR":""})

    return jsonify({"ERROR":"Nao tem email cadastrado"})

@app.route('/api/get/alldados', methods=['GET'])
def getAll():
    try:
        tup = c.getAllDados()
        list_json = []
        for t in tup:
            list_json.append({'idDado':t[0], 'idUser':t[1], 'valor1':t[2], 'valor2':t[3],'data':t[4], 'tipo':t[5]})
        return jsonify({"ERROR":"", "len":len(list_json), "Data":list_json})
    except: return jsonify({"ERROR":"problema de autenticacao"})

#excluir dado específico do usuário
@app.route("/api/delete/dado/<id_user>/<id_dado>", methods=["DELETE"])
def deleteDadoID(id_user, id_dado):
    return jsonify(c.deleteDado(id_user, id_dado))

#excluir todos os dados do usuário
@app.route("/api/delete/alldados/<id_user>", methods=["DELETE"])
def deleteAll(id_user):
    return jsonify(c.deleteAllMyDados(id_user))

@app.route('/api/generatedata', methods=['POST'])
def generateData():
    request_data = request.get_json()

    id_user = request_data['id_user']
    qnt_valores = request_data["qtValores"]
    min_minutos = request_data["minMinutos"]
    max_minutos = request_data["maxMinutos"]
    tipo = request_data["tipo"]

    if (tipo == 'TC'):
        utils.TemperaturaCorporal(id_user, qnt_valores, min_minutos, max_minutos)
    elif (tipo == 'PA'):
        utils.PA(id_user, qnt_valores, min_minutos, max_minutos)
    elif (tipo == 'SP02'):
        utils.SP02(id_user, qnt_valores, min_minutos, max_minutos)
    else:
        return jsonify({"ERROR":"Tipo deo Sensor é invalido! Permitidos [TC, PA, SP02]", "Status":0})

    return jsonify({"ERROR":"", "Status":1})

@app.route("/api/situacoesEspecifcas/<id_user>", methods=["GET"])
def getSituacoesEspecifcas(id_user):
    utils.verificarSituacoesEspecificas(id_user)
    return jsonify({"ERROR":"", "Status":1})

@app.route("/api/dadosSituacao1/<id_user>", methods=["GET"])
def getDadosSituacao1(id_user):
    try:
        tup = c.getDadosSituacaoEspecifica1(id_user)
        list_json = []
        for t in tup:
            list_json.append({'idDado':t[0], 'idUser':t[1], 'valor1':t[2], 'valor2':t[3],'data':t[4], 'tipo':t[5]})

        return jsonify({"ERROR":"", "len": len(list_json), "Data":list_json})
    except:
        return jsonify({"ERROR":"Erro ao buscar os dados", "Status":0})

@app.route("/api/dadosSituacao2/<id_user>", methods=["GET"])
def getDadosSituacao2(id_user):
    try:
        tup = c.getDadosSituacaoEspecifica2(id_user)
        list_json = []
        for t in tup:
            list_json.append({'sistolica': t[1], 'diastolica': t[2], 'data': t[3]})

        return jsonify({"ERROR":"", "len": len(list_json), "Data":list_json})
    except: 
        return jsonify({"ERROR":"Erro ao buscar os dados", "Status":0})

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>API nao reconhece esse endpoint</p>", 404

app.run()
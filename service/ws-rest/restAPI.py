import json
import pymysql
from flask import request, jsonify
import flask
import datetime
from flask_cors import CORS

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config["DEBUG"] = True

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

    def addDados(self, id_user, value1, value2, type_):
        if self.verifyUserExists(id_user) == 0: return {"ERROR": 'Usuario nao cadastrado'}
        conexao = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_add = conexao.cursor()
        sql = "INSERT INTO DadosColetados (usuario, valor1, valor2, tipo) VALUES (%s,%s,%s,%s)"
        data = (id_user, value1, value2, type_)
        cursor_add.execute(sql, data)
        conexao.commit()
        cursor_add.close()
        conexao.close()
        return {"ERROR":"", "Status":1}

    def changeDados(self, id_user, id_dado, valor1='', valor2='', tipo=''):
        if self.verifyUserExists(id_user) == 0: return {"ERROR": 'Usuario nao cadastrado'}
        if self.verifyDados(id_dado) == 0:return {"ERROR": 'Dado nao cadastrado'}
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

c = BD()


#@app.route('/api/get/users', methods=['GET'])
#def getUsersAndDadosBD():
#    tup = c.getUsersAndDados()
#    list_json = []
#    for t in tup:
#        list_json.append({'id_user':t[0], 'name':t[1], 'born':t[2], 'sex':t[3]})
#    return jsonify(list_json)

@app.route('/api/add', methods=['PUT'])
def insertDados():
    user = request.form.get('id_user')
    if user == None or user == '': return jsonify({"ERROR":"ID usuario invalido", "Status":0})
    valor1 = request.form.get('valor1')
    s_error = ''
    if valor1 == '' or valor1 == None:
        s_error += 'Insira o valor 1. '
        #return jsonify({"ERROR":"Insira o valor 1", "Status":0})
    valor2 = request.form.get('valor2')
    if valor2 == '' or valor2 == None:
		valor2 = '' 
        #s_error +='Insira o valor 2. '
        #return jsonify({"ERROR":"Insira o valor 2", "Status":0})
    tipo = request.form.get('tipo')
    if tipo == '' or tipo == None:
        s_error +='Insira o tipo.'
        #return jsonify({"ERROR":"Insira o tipo", "Status":0})
    if len(s_error) > 1:return jsonify({"ERROR":s_error.strip(), "Status":0})
    r = c.addDados(user, valor1, valor2, tipo)
    return jsonify(r)

@app.route('/api/change/mydados', methods=['POST'])
def changeMyDados():
    id_dado = request.form.get('id_dado')
    id_user = request.form.get('id_user')
    valor1 = request.form.get('valor1')
    valor2 = request.form.get('valor2')
    tipo = request.form.get('tipo')
    valor1 = valor1 if valor1!=None else ''
    valor2 = valor2 if valor2!=None else ''
    tipo = tipo if tipo!=None else ''
    if id_user == None: return jsonify({"error":'ERROR ID USER'})
    if id_dado == None: return jsonify({"error":'ERROR ID DADO'})
    if valor1 == '' and valor2 == '' and tipo == '':
        return jsonify({"ERROR":'Nenhum dado a ser alterado', 'Status':0})
    r = c.changeDados(id_user, id_dado, valor1, valor2, tipo)
    return jsonify(r)


#http://127.0.0.1:5000/api/get/mydado?iduser=1&iddado=2
@app.route('/api/get/mydado', methods=['GET'])
def getDadosUnique():
    id_user_get = request.args.get('iduser', type=int)
    id_dado_get = request.args.get('iddado', type=int)
    if (id_user_get == '' or id_user_get == None) and (id_dado_get == '' or id_dado_get == None): return jsonify({"ERROR": "ID usuario e ID dado invalido"})
    try:int(id_user_get)
    except:return jsonify({"ERROR": "ID usuario invalido"})
    try:int(id_dado_get)    
    except:return jsonify({"ERROR": "ID dado invalido"})
    if id_user_get == '': return jsonify({"ERROR": "ID usuario invalido"})
    if id_dado_get == '': return jsonify({"ERROR": "ID dado invalido"})
    tup = c.getMyDadoSpecify(id_user_get, id_dado_get)
    #if tup ==  -1:
        #return jsonify({"ERROR":"Usuario nao existe", "Status":0})
    #if tup ==  -2:
        #return jsonify({"ERROR":"Dado nao existe", "Status":0})
    #if len(tup) == 0: return jsonify({"ERROR": 'Nenhum dado encontrado', 'Status':0})
    if tup ==  -1 or tup ==  -2:return jsonify({"ERROR": 'Nenhum dado encontrado', 'Status':0})
    list_json = []
    for t in tup:
        #list_json.append({'idDado':t[0], 'idUser':t[1], 'valor1':t[2], 'valor2':t[3],'data':t[4], 'tipo':t[5]})
        list_json.append({'valor1':t[2], 'valor2':t[3],'data':t[4], 'tipo':t[5]})
    return jsonify({"ERROR":"", "Data":list_json})


@app.route('/api/get/mydado', methods=['POST'])
def getDadosUniqueWithPOST():
    id_user_post = request.form.get('id_user')
    id_dado_post = request.form.get('id_dado')
    if id_user_post == None and id_dado_post == None: return jsonify({"ERROR": "ID usuario e ID dado invalido"})
    if id_user_post == None: return jsonify({"ERROR": "ID usuario invalido"})
    if id_dado_post == None: return jsonify({"ERROR": "ID dado invalido"})
    print("TIP")
    tup = c.getMyDadoSpecify(id_user_post, id_dado_post)
    print("TIP", tup)
    #if tup ==  -1:
        #return jsonify({"ERROR":"Usuario nao existe", "Status":0})
    #if tup ==  -2:
        #return jsonify({"ERROR":"Dado nao existe", "Status":0})
    #if len(tup) == 0: return jsonify({"ERROR": 'Nenhum dado encontrado', 'Status':0})
    if tup ==  -1 or tup ==  -2:return jsonify({"ERROR": 'Nenhum dado encontrado', 'Status':0})
    list_json = []
    for t in tup:
        list_json.append({'idDado':t[0], 'idUser':t[1], 'valor1':t[2], 'valor2':t[3],'data':t[4], 'tipo':t[5]})
    return jsonify({"ERROR":"", "len":len(list_json), "Data":list_json})


@app.route('/api/get/mydados', methods=['POST'])
def getDados():
    id_user_post = request.form.get('id_user')
    if id_user_post == None: return jsonify({"ERROR": "ID usuario invalido"})
    tup = c.getMyAllDados(id_user_post)
    if tup == -1: return jsonify({"ERROR": "Usuario nao existe"})
    list_json = []
    for t in tup:
        list_json.append({'idDado':t[0], 'idUser':t[1], 'valor1':t[2], 'valor2':t[3],'data':t[4], 'tipo':t[5]})
    return jsonify({"ERROR":"", "len":len(list_json), "Data":list_json})

@app.route('/api/get/alldados', methods=['GET'])
def getAll():
    try:
        tup = c.getAllDados()
        list_json = []
        for t in tup:
            list_json.append({'idDado':t[0], 'idUser':t[1], 'valor1':t[2], 'valor2':t[3],'data':t[4], 'tipo':t[5]})
        return jsonify({"ERROR":"", "len":len(list_json), "Data":list_json})
    except: return {"ERROR":"problema de autenticacao"}

#excluir dado específico do usuário
@app.route("/api/delete/dado/<id_user>/<id_dado>", methods=["DELETE"])
def deleteDadoID(id_user, id_dado):
    return jsonify(c.deleteDado(id_user, id_dado))

##excluir todos os dados do usuário
@app.route("/api/delete/alldados/<id_user>", methods=["DELETE"])
def deleteAll(id_user):
    return jsonify(c.deleteAllMyDados(id_user))


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>API nao reconhece esse endpoint</p>", 404

app.run()
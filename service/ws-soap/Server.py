from typing import Tuple
import logging
import datetime
from spyne import Application, rpc, ServiceBase, Unicode, Iterable
from spyne.model.complex import Array
from spyne.protocol.xml import XmlDocument
from spyne.protocol.soap import Soap12
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import json
import pymysql


ENDPOINT="aws-db.cu6xdlhm2sr3.us-east-2.rds.amazonaws.com"
PORT=3306
USR="admin"
REGION="us-east-2b"
DBNAME="iomt"

class BD(object):

    def verifyExists(self, id_user):
        conn_ver = pymysql.connect(host=ENDPOINT, user=USR, passwd="admin1234", port=PORT, database=DBNAME)
        cursor_ver = conn_ver.cursor()
        sql = "select id FROM usuario WHERE id = %s"
        data = (id_user)
        cursor_ver.execute(sql, data)
        #quando não existir o id
        if cursor_ver.rowcount==0:
            cursor_ver.close()
            conn_ver.close()
            return 0
        else:
            cursor_ver.close()
            conn_ver.close()
            return 1

c = BD()


class Usuarios(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=int)
    def addUser(self, nome, nascimento, sexo, email):
        try:
            conexao = pymysql.connect(host=ENDPOINT, user=USR, passwd="admin1234", port=PORT, database=DBNAME)
            cursor_add = conexao.cursor()
            sql = "INSERT INTO usuario (nome, nascimento, sexo, email) VALUES (%s, %s, %s, %s)"
            data = (nome,nascimento,sexo, email)
            cursor_add.execute(sql, data)
            conexao.commit()
            cursor_add.close()
            conexao.close()
            return 1
        except: return 0

    @rpc(int, Unicode, Unicode, Unicode,Unicode, _returns=int)
    def alterInfosUser(self, id_user, name='', nascimento='', sexo='', email=''):
        #usuário não existe? se não, retorna 0. Caso contrário, retorna 1 (deu certo)
        if c.verifyExists(id_user) == 0: return 0
        try:
            connection = pymysql.connect(host=ENDPOINT, user=USR, passwd="admin1234", port=PORT, database=DBNAME)
            cursor = connection.cursor()
            data = ()
            sql_parcial = "UPDATE usuario SET"
            if name != '':
                sql_parcial +=  " nome = %s" 
                data = data + (name,)
            if nascimento != '':
                if 'nome' in sql_parcial:sql_parcial +=','
                sql_parcial += " nascimento = %s"
                data = data + (nascimento,)
            if sexo != '':
                if 'nome' in sql_parcial or 'nascimento' in sql_parcial:sql_parcial +=','
                sql_parcial += " sexo = %s"
                data = data + (sexo,)
            if email != '':
                if 'nome' in sql_parcial or 'nascimento' in sql_parcial or 'sexo' in sql_parcial:sql_parcial +=','
                sql_parcial += " email = %s"
                data = data + (email,)
            sql_completo = sql_parcial + ' WHERE id = %s'
            data = data + (str(id_user),)
            cursor.execute(sql_completo, data)
            connection.commit()
            cursor.close()
            connection.close()
            return 1
        except: return 0

    @rpc(int, _returns=Iterable(Unicode))
    def getOneUser(self, id_user):
        if c.verifyExists(id_user) == 0: return tuple(map(str, ['Usuario nao existe']))
        conexao_getone = pymysql.connect(host=ENDPOINT, user=USR, passwd="admin1234", port=PORT, database=DBNAME)
        cursor_getone = conexao_getone.cursor()
        sql = "SELECT * FROM usuario WHERE id=%s"
        cursor_getone.execute(sql, (id_user))
        results_one = cursor_getone.fetchall()
        cursor_getone.close()
        conexao_getone.close()
        resultado_final = []
        for j in range(len(results_one)):
            resultado_final.append((results_one[j][0], results_one[j][1], results_one[j][2].strftime('%d-%m-%Y'), results_one[j][3], results_one[j][4]))
        return tuple(map(str, resultado_final))

    @rpc(_returns=Iterable(Unicode))
    def getAllUsers(self):
        conexao_getall = pymysql.connect(host=ENDPOINT, user=USR, passwd="admin1234", port=PORT, database=DBNAME)
        cursor_getall = conexao_getall.cursor()
        sql = "SELECT * FROM usuario"
        cursor_getall.execute(sql)
        results_all = cursor_getall.fetchall()
        cursor_getall.close()
        conexao_getall.close()
        resultado_final = []
        for j in range(len(results_all)):
            resultado_final.append((results_all[j][0], results_all[j][1], results_all[j][2].strftime('%d-%m-%Y'), results_all[j][3], results_all[j][4]))
        return tuple(map(str, resultado_final))

    #se o usuário não existe, então retorna 0. Caso contrário, retorna 1
    @rpc(int, _returns=int)
    def deleteUser(self, id_user):
        #usuário existe?
        if c.verifyExists(id_user) == 0:
            return 0
        try:
            conn = pymysql.connect(host=ENDPOINT, user=USR, passwd="admin1234", port=PORT, database=DBNAME)
            cursor = conn.cursor()
            sql = "DELETE FROM usuario WHERE id = %s"
            data = (id_user)
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()
            return 1
        except: return 0


application = Application([Usuarios], 'spyne.examples.hello.soap',
                          in_protocol=Soap12(validator='lxml'),
                          out_protocol=Soap12())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':

    print ("listening to http://127.0.0.2:8000")
    print ("wsdl is at: http://localhost:8000/?wsdl")
    #logging.basicConfig(level=logging.DEBUG)
    #logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    server = make_server('127.0.0.2', 8000, wsgi_application)
    server.serve_forever()

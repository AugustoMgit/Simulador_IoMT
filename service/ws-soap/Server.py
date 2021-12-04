from typing import Tuple
from spyne import Application, rpc, ServiceBase, Unicode, Iterable
from spyne.model.complex import Array, ComplexModel, ComplexModelBase
from spyne.protocol.soap import Soap12
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import json
import pymysql

class CorsService(ServiceBase):
    origin = '*'

def _on_method_return_object(ctx):
    print("hello")
    ctx.transport.resp_headers['Access-Control-Allow-Origin'] = \
                                              ctx.descriptor.service_class.origin

CorsService.event_manager.add_listener('method_return_object',
                                                        _on_method_return_object)


class BD(object):

    def verifyExists(self, id_user):
        conn_ver = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
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

    @rpc(Unicode, Unicode, Unicode, _returns=int)
    def addUser(self, nome, nascimento, sexo):
        print("opaa")
        conexao = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_add = conexao.cursor()
        sql = "INSERT INTO usuario (nome, nascimento, sexo) VALUES (%s, %s, %s)"
        data = (nome,nascimento,sexo)
        cursor_add.execute(sql, data)
        conexao.commit()
        cursor_add.close()
        conexao.close()
        return 1

    @rpc(int, Unicode, Unicode, Unicode, _returns=int)
    def alterInfosUser(self, id_user, name='', nascimento='', sexo=''):
        #usuário não existe? se não, retorna 0. Caso contrário, retorna 1 (deu certo)
        if c.verifyExists(id_user) == 0: return 0
        connection = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
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
        sql_completo = sql_parcial + ' WHERE id = %s'
        data = data + (str(id_user),)
        cursor.execute(sql_completo, data)
        connection.commit()
        cursor.close()
        connection.close()
        return 1

    @rpc(int, _returns=Iterable(Unicode))
    def getOneUser(self, id_user):
        if c.verifyExists(id_user) == 0:return 0
        conexao_getone = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_getone = conexao_getone.cursor()
        sql = "SELECT * FROM usuario WHERE id=%s"
        cursor_getone.execute(sql, (id_user))
        results_one = cursor_getone.fetchall()
        cursor_getone.close()
        conexao_getone.close()
        return tuple(map(str, results_one))

    @rpc(_returns=Iterable(Unicode))
    def getAllUsers(self):
        conexao_getall = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor_getall = conexao_getall.cursor()
        sql = "SELECT * FROM usuario"
        cursor_getall.execute(sql)
        results_all = cursor_getall.fetchall()
        cursor_getall.close()
        conexao_getall.close()
        return tuple(map(str, results_all))

    #se o usuário não existe, então retorna 0. Caso contrário, retorna 1
    @rpc(int, _returns=int)
    def deleteUser(self, id_user):
        #usuário existe?
        if c.verifyExists(id_user) == 0:
            return 0
        conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="iomt",autocommit=True)
        cursor = conn.cursor()
        sql = "DELETE FROM usuario WHERE id = %s"
        data = (id_user)
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()
        return 1


application = Application([Usuarios], 'spyne.examples.hello.soap',
                          in_protocol=Soap12(validator='lxml'),
                          out_protocol=Soap12())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    print ("listening to http://127.0.0.2:8000")
    print ("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.2', 8000, wsgi_application)
    server.serve_forever()
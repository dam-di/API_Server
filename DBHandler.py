from pymongo import MongoClient

from ResponseModel import ResponseModel

class DBHandler(object):
    def __init__(self):
        self.db = self.conectar()
        self.collection = self.db.get_collection('datos')


    def conectar(self):
        client = MongoClient(
            host = 'infsalinas.sytes.net:10450',
            #host = '192.168.1.100:10450',
            serverSelectionTimeoutMS = 3000,
            username = '',
            password = '',
            authSource = ''
        )
        db = client.get_database('1damX')
        return db

    def insertarDatos(self, datos):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('datos')
            self.collection.insert_one(datos)
            response.resultOk = True
            response.data = 'Datos insertados con exito'
        except Exception as e:
            print(e)

        return response


    def obtenerListaDatos(self):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('datos')
            listaDatos = []
            coleccion = self.collection.find({})
            for dato in coleccion:
                listaDatos.append(dato)

            response.resultOk = True
            response.data = str(listaDatos)
            print(listaDatos)
        except Exception as e:
            print(e)

        return response
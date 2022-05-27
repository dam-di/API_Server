import json
from flask import Flask, request
from ResponseModel import ResponseModel
from DBHandler import DBHandler

app = Flask(__name__)


@app.route('/rutaDatos', methods=['POST', 'PUT', 'DELETE', 'GET'])
def rutaDatos():
    print("ENTRA EN LA RUTA")
    print(request.json)
    response = ResponseModel()
    datos = request.json['data']
    metodo = request.json['method']

    if metodo == 'POST':
        response = insertarDatos(datos)
    elif metodo == 'GET':
        response = obtenerListaDatos(datos)
    elif metodo == 'PUT':
        pass
    elif metodo == 'DELETE':
        pass
    print('Estas devolviendo')
    print(response.__dict__)
    return json.dumps(response.__dict__)

def insertarDatos(datos):
    response = DBHandler().insertarDatos(datos)
    return response


def obtenerListaDatos(_idD):
    print('Obtener lista datos')
    if _idD == 'all':
        response = DBHandler().obtenerListaDatos()
    else:
        #TODO
        response = DBHandler().obtenerListaDatos()
    return response



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')
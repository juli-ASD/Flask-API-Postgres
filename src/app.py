from types import MethodType
from flask import Flask, jsonify, request
from db import Session, engine
from models import Usuario
import json

app = Flask(__name__)  #Crear app

session = Session()  #Crear session

#Metodo get para probar conección con la base de datos
@app.route('/', methods=['GET']) 
def ping():
    return jsonify({"response": "El método GET responde en Flaskapi"}) #Retornar archivo JSON a Postman

#Método post para crear usuario en la base de datos
@app.route('/create_user' ,methods=['POST']) 
def create_user():
    
    data = json.loads(request.data)  #Diccionario, recibido de mensaje JSON desde postman
    #Manejo de errores y respuestas a peticiones POST
    if 'username' not in data :
        return jsonify({"response": "No está enviando el username"})
    if 'email' not in data :
        return jsonify({"response": "No está enviando el email"})
    if len(data["username"]) ==0 :
        return jsonify({"response": "Username no puede estar vacio"})
    if len(data["email"]) ==0 :
        return jsonify({"response": "Email no puede estar vacio"})
    with engine.connect() as con:
        new_user = Usuario(username=data["username"],email=data["email"]) #Crear objeto nuevo usuario
        session.add(new_user)  #Añadir nuevo usuario a la session
        try:
            session.commit()  #Crear usuario en la tabla (Postgres)
        except:
            return jsonify({"response": "Ya está creado el usuario en Flaskapi"})
    return jsonify({"response": "Se creó el usuario en Flaskapi"})

#Arrancar y mantener app incicada 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


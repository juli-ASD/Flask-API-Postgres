from types import MethodType
from flask import Flask, jsonify, request
from db import Session, engine
from models import Usuario
import json

app = Flask(__name__)

session = Session()

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "El método GET responde en Flaskapi"})

@app.route('/create_user' ,methods=['POST'])
def create_user():
    
    data = json.loads(request.data)
    if 'username' not in data :
        return jsonify({"response": "No está enviando el username"})
    if 'email' not in data :
        return jsonify({"response": "No está enviando el email"})
    if len(data["username"]) ==0 :
        return jsonify({"response": "Username no puede estar vacio"})
    if len(data["email"]) ==0 :
        return jsonify({"response": "Email no puede estar vacio"})
    print(data)
    print(type(data))
    with engine.connect() as con:
        new_user = Usuario(username=data["username"],email=data["email"])
        session.add(new_user)
        try:
            session.commit()
        except:
            return jsonify({"response": "Ya está creado el usuario en Flaskapi"})
    return jsonify({"response": "Se creó el usuario en Flaskapi"})


if __name__ == '__main__':
    app.run(debug=True)


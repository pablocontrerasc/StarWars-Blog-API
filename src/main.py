"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Usuario, Personaje, Planeta, PersonajeFavoritos, PlanetaFavoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/users', methods=['GET'])
def get_user():

    usuario = Usuario.query.all()
    response_body = list(map(lambda x: x.serialize(), usuario))
 
    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def get_people():
    personaje = Personaje.query.all()
    response_body = list(map(lambda x: x.serialize(), personaje))
    return jsonify(response_body), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_one_people(people_id):
    personaje = Personaje.query.get(id = people_id)
    response_body = list(map(lambda x: x.serialize(), personaje))
    return jsonify(response_body), 200

@app.route('/planet', methods=['GET'])
def get_planet():
    planeta = Planeta.query.all()
    response_body = list(map(lambda x: x.serialize(), planeta))
    return jsonify(response_body), 200

@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    planeta = Planeta.query.filter_by(id = planet_id)
    response_body = list(map(lambda x: x.serialize(), planeta))
    return jsonify(response_body), 200

@app.route('/users/favorites', methods=['GET'])
def get_users_favorites():
    usuario_id= request.json.get("usuario_id")

    personajes = PersonajeFavoritos.query.filter_by(usuario_id= usuario_id)
    lista_personajes = list(map(lambda x: x.serialize(), personajes))

    planetas = PlanetaFavoritos.query.filter_by(usuario_id= usuario_id)
    lista_planetas = list(map(lambda x: x.serialize(), planetas))

    response_body = {
        "Personajes_favoritos": lista_personajes,
        "Planetas_favoritos": lista_planetas
    }

    return  jsonify(response_body), 200

@app.route("/users", methods=["POST"])
def new_user():
    try:
        nombre = request.json.get("nombre", None)
        apellido = request.json.get("apellido", None)
        email = request.json.get("email", None)
        password = request.json.get("password", None)
        fecha_subscripcion = request.json.get("fecha_subscripcion", None)
       
        userR = Usuario.query.filter_by(email=email).first()
        if userR:
            return {"Error": "Correo ya registrado"}
        user = Usuario(
            nombre=nombre, apellido=apellido, email=email, password=password, fecha_subscripcion=fecha_subscripcion
        )
        db.session.add(user)
        db.session.commit()
        return {"mensaje": "ok"}, 200
    except Exception as e:
        print(f"new_user_ERROR: {e}")
        return (f"new_user_ERROR: {e}"), 500


@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id): 
    usuario_id = request.json.get("usuario_id")
    planeta_favorito = PlanetaFavoritos(usuario_id, planeta_id=planet_id)
    db.session.add(planeta_favorito)
    db.session.commit()
    return "Planeta favorito agregado", 200

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_peple(people_id): 
    usuario_id = request.json.get("usuario_id")
    personaje_favorito = PersonajeFavoritos(usuario_id, personaje_id=people_id)
    db.session.add(personaje_favorito)
    db.session.commit()
    return "Personaje favorito agregado", 200


@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id): 
    usuario_id = request.json.get("usuario_id")
    planeta_favorito = PlanetaFavoritos.query.filter_by(usuario_id = usuario_id, planeta_id=planet_id).first()
    db.session.delete(planeta_favorito)
    db.session.commit()
    return "Planeta favorito eliminado", 200

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id): 
    usuario_id = request.json.get("usuario_id")
    personaje_favorito = PersonajeFavoritos.query.filter_by(usuario_id = usuario_id, personaje_id=people_id).first()
    print(personaje_favorito,"planteFF")
    db.session.delete(personaje_favorito)
    db.session.commit()
    return "Planeta favorito eliminado", 200
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

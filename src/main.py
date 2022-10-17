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
from models import db, User, Characters, Planets, FavouritePlanets, FavouriteCharacters 
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

#-------------- AQUI VAN LOS USERS--------------

@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.filter().all()
    print(users)
    result = list(map(lambda user: user.serialize(), users))
    print(result)
    response_body = {
        "users": result,
    }

    return jsonify(result), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    print(user)
    print(user.serialize())
    
    result = {
        "msg": f'numero de usuario: {user_id}'
    }

    return jsonify(user.serialize()), 200

#============= AQUI VAN LOS PLANETAS=============#

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.filter().all()
    print(planets)
    result = list(map(lambda planet: planet.serialize(), planets))
    print(result)
    response_body = {
    "msg": "Hello, this is your GET /user response "
    }

    return jsonify(result), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.get(planet_id)
    print(planet)
    print(planet.serialize())
    
    result = {
        "msg": f'numero de planeta: {planet_id}'
    }

    return jsonify(user.serialize()), 200

#============= AQUI VAN LOS PERSONAJES=============#

@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.filter().all()
    print(characters)
    result = list(map(lambda character: character.serialize(), characters))
    print(result)
    response_body = {
    "msg": "Hello, this is your GET /user response "
    }

    return jsonify(result), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Characters.query.get(character_id)
    print(character)
    print(character.serialize())
    
    result = {
        "msg": f'numero de usuario: {character_id}'
    }

    return jsonify(user.serialize()), 200

#============= AQUI VAN LOS PERSONAJES FAVORITOS=============#

@app.route('/user/favourites/characters', methods=['GET'])
def get_fav_characters():
    character = FavouriteCharacters.query.filter().all()
    print(character)
    result = list(map(lambda character: character.serialize(), character))
    print(result)
    response_body = {
    "msg": "Hello, this is your GET /user response "
    }

    return jsonify(result), 200

@app.route('/user/<int:user_id>/favourites/characters/<int:character_id>', methods=['POST'])
def add_fav_characters(user_id, character_id):
    fav_characters = FavouriteCharacters(user_id=int(user_id), character_id=int(character_id))
    db.session.add(fav_characters)
    db.session.commit()
    response_body = {
        "msg": "Favorito agregado"
    }
    return jsonify(response_body), 200

@app.route('/user/<int:user_id>/favourites/characters/<int:character_id>', methods=['DELETE'])
def delete_fav_characters(user_id, character_id):
    delete_characters = FavouriteCharacters.query.filter_by(character_id=character_id, user_id=user_id).first()
    db.session.delete(delete_characters)
    db.session.commit()
    response_body = {
        "msg": "Favorito borrado"
    }
    return jsonify(response_body), 200

#============= AQUI VAN LOS PLANETAS FAVORITOS=============#

@app.route('/user/favourites/planets', methods=['GET'])
def get_fav_planets():
    planet = FavouritePlanets.query.filter().all()
    print(planet)
    result = list(map(lambda planet: planet.serialize(), planet))
    print(result)
    response_body = {
    "msg": "Hello, this is your GET /user response "
    }

    return jsonify(result), 200

@app.route('/user/<int:user_id>/favourites/planets/<int:planet_id>', methods=['POST'])
def add_fav_planets(user_id, planet_id):
    fav_planets = FavouritePlanets(user_id=int(user_id), planet_id=int(planet_id))
    db.session.add(fav_planets)
    db.session.commit()
    response_body = {
        "msg": "Favorito agregado"
    }
    return jsonify(response_body), 200

@app.route('/user/<int:user_id>/favourites/planets/<int:planet_id>', methods=['DELETE'])
def delete_fav_planet(user_id, planet_id):
    delete_planets = FavouritePlanets.query.filter_by(planet_id=planet_id, user_id=user_id).first()
    db.session.delete(delete_planets)
    db.session.commit()
    response_body = {
        "msg": "Favorito borrado"
    }
    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

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
from models import db, User, People, Planet, Fav_people, Fav_planet


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

#FALTA POR HACER
@app.route('/users', methods=['GET'])
def get_users():
    alluser = User.query.all()
    alluser = list(map(lambda elemento: elemento.serialize(), alluser))

    return jsonify({"Usuarios" : alluser}), 200

@app.route('/users/favourites', methods=['GET'])
def get_favourites():
    allfavourites = Fav_people.query.all()
    allfavourites = list(map(lambda elemento: elemento.serialize(), allfavourites))
    peoples = []
    for e in allfavourites:

        contador = 0
        contador2 = 0

        for i in e:

            contador += 1

            if i == "people_id":

                diccionary = {}
                print (e[i])
                contador2 += 1
                print(f"Identifica {contador2} veces")
                people = People.query.filter_by(id = e[i])
                people = list(map(lambda elemento: elemento.serialize(), people))

                for el in people:

                    for key in el:

                        print(key)
                        print(el[key])
                        diccionary[key] = el[key]
                        print(diccionary)

                peoples.append(diccionary)
                print(peoples)

    allfavourite = Fav_planet.query.all()
    allfavourite = list(map(lambda elemento: elemento.serialize(), allfavourite))
    for e in allfavourite:

        contador = 0
        contador2 = 0

        for i in e:

            contador += 1

            if i == "planet_id":

                diccionary = {}
                print (e[i])
                contador2 += 1
                print(f"Identifica {contador2} veces")
                people = Planet.query.filter_by(id = e[i])
                people = list(map(lambda elemento: elemento.serialize(), people))

                for el in people:

                    for key in el:

                        print(key)
                        print(el[key])
                        diccionary[key] = el[key]
                        print(diccionary)

                peoples.append(diccionary)
                # print(peoples)
                
    return jsonify({"Personajes y planetas favoritos" : peoples}), 200         


#Lista todos los registros de People en la BBDD
@app.route('/people', methods=['GET'])
def get_people():
    allpeople = People.query.all() #retorna un arreglo de clases 
    allpeople = list(map(lambda elemento: elemento.serialize(), allpeople)) #itero en cada una de las clases y almaceno el resultado de la funcion serialize
    print(allpeople)
    return jsonify({"resultado": allpeople})

#Lista todos los registros de Planet en la BBDD
@app.route('/planet', methods=['GET'])
def get_planet():
    allplanet = Planet.query.all() #retorna un arreglo de clases 
    allplanet = list(map(lambda elemento: elemento.serialize(), allplanet)) #itero en cada una de las clases y almaceno el resultado de la funcion serialize
    print(allplanet)
    return jsonify({"resultado": allplanet})

#Lista un el registro indicado de la tabla People
@app.route('/people/<int:id>', methods=['GET'])
def get_one_people(id):

    onepeople = People.query.get(id)
    if onepeople:
        onepeople = onepeople.serialize()
        return jsonify({"resultado": onepeople})
    else:
        return jsonify({"resultado": "personaje no existe"})

#Lista un el registro indicado de la tabla Planet
@app.route('/planet/<int:id>', methods=['GET'])
def get_one_planet(id):

    oneplanet = Planet.query.get(id)
    if oneplanet:
        oneplanet = oneplanet.serialize()
        return jsonify({"resultado": oneplanet})
    else:
        return jsonify({"resultado": "planeta no existe"})

#Añade una nueva fila (people) a la tabla Fav_people
@app.route('/favourite/people/<int:people_id>', methods = ['POST'])
def add_fav_people(people_id):
    onepeople = People.query.get(people_id)
    if onepeople:
        new = Fav_people()
        new.user_id = 1
        new.people_id = people_id
        db.session.add(new)#agrego el registro a la base de datos
        db.session.commit()#guardar los cambios realizados
        return jsonify({"resultado": "Todo salio bien"})
    else:
        return jsonify({"resultado": "el personaje no existe"})

#Añade una nueva fila (planet) a la tabla Fav_planet
@app.route('/favourite/planet/<int:planet_id>', methods = ['POST'])
def add_fav_planet(planet_id):
    oneplanet = Planet.query.get(planet_id)
    if oneplanet:
        new = Fav_planet()
        new.user_id = 1
        new.planet_id = planet_id
        db.session.add(new)#agrego el registro a la base de datos
        db.session.commit()#guardar los cambios realizados
        return jsonify({"resultado": "Todo salio bien"})
    else:
        return jsonify({"resultado": "el planeta no existe"})

#Elimina el personaje cuyo índice es idicado
@app.route('/favourite/people/<int:people_id>', methods = ['DELETE'])
def delete_fav_people(people_id):
    onepeople = Fav_people.query.get(people_id)
    print(onepeople)
    db.session.delete(onepeople)
    db.session.commit()
    onepeople = onepeople.serialize()
    return jsonify({"Ha sido borrado el personaje": onepeople})
    
#Elimina el planeta cuyo índice es idicado
@app.route('/favourite/planet/<int:planet_id>', methods = ['DELETE'])
def delete_fav_planet(planet_id):
    oneplanet = Fav_planet.query.get(planet_id)
    print(oneplanet)
    db.session.delete(oneplanet)
    db.session.commit()
    oneplanet = oneplanet.serialize()
    return jsonify({"Ha sido borrado el planeta": oneplanet})

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

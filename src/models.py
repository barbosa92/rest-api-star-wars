from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique=True, nullable=False)#no puede ser nulo este campo
    gender = db.Column(db.String(120), unique=False, nullable=True)#puede dejarse el campo vacío
    hair_color = db.Column(db.String(120), unique=False, nullable=True)#puede dejarse el campo vacío

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
        }

class Planet (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique=True, nullable=False)#no puede ser nulo este campo
    diameter = db.Column(db.Integer, unique=False, nullable=False)#puede dejarse el campo vacío
    climate = db.Column(db.String(120), unique=False, nullable=False)#puede dejarse el campo vacío
    terrain = db.Column(db.String(120), unique=False, nullable=False)#puede dejarse el campo vacío
    population = db.Column(db.String(120), unique=False, nullable=False)#puede dejarse el campo vacío
    inhabitants = db.Column(db.String(250), unique=False, nullable=True)#puede dejarse el campo vacío

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.diameter,
            "diameter": self.diameter,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
        }

class Fav_people(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #quien le dio a favorito
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #quien es el favorito
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    #defino las relaciones
    rel_user = db.relationship(User)
    rel_people = db.relationship(People)

    def __repr__(self):
        return '<FavPeople %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
         
            # do not serialize the password, its a security breach
        }
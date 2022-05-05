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

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    fecha_subscripcion = db.Column(db.String(100))
    
    def __init__(self,nombre,apellido,email, password,fecha_subscripcion):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.fecha_subscripcion = fecha_subscripcion

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "fecha_subscripcion": self.fecha_subscripcion
        }


class Personaje(db.Model):
    __tablename__ = 'personaje'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    height = db.Column(db.String(100))
    mass = db.Column(db.String(100))
    hair_color = db.Column(db.String(100))
    skin_color = db.Column(db.String(100))
    eye_color = db.Column(db.String(100))
    birth_year = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    homeworld = db.Column(db.String(150))
    created = db.Column(db.String(100))

    def __init__(self, id, name, height, mass, hair_color, skin_color, eye_color,birth_year,gender,homeworld,created):
        self.id = id
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.created = created
    
    def __repr__(self):
        return '<Personaje %r>' % self.name

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "heigth": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_yeear": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "creatd": self.created
        }

class Planeta(db.Model):
    __tablename__ = 'planeta'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    orbital_period = db.Column(db.String(100))
    rotation_period = db.Column(db.String(100))
    diameter = db.Column(db.String(100))
    climate = db.Column(db.String(100))
    gravity = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    surface_water = db.Column(db.String(100))
    population = db.Column(db.String(100))
    created = db.Column(db.String(100))

    def __init__(self, name, orbital_period, rotation_period, diameter, climate, gravity, terrain,surface_water, population, created):
        self.name = name
        self.orbital_period = orbital_period
        self.rotation_period = rotation_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.surface_water = surface_water
        self.population = population
        self.created = created
    
    def __repr__(self):
        return '<Planeta %r>' % self.name

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "surface_water":self.surface_water,
            "papularion": self.population,
            "created": self.created

        }
    
class PlanetaFavoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = "planeta_favoritos"
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    planeta_id = db.Column(db.Integer, nullable=False)

    def __init__(self, usuario_id, planeta_id):
        self.usuario_id = usuario_id
        self.planeta_id = planeta_id

    def __repr__(self):
        return '<PlanetaFavoritos %r>' % self.planeta_id

    def serialize(self):
        return {
            "planeta_id": self.planeta_id,
            "usuario_id": self.usuario_id
        }

class PersonajeFavoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = "personaje_favoritos"
    usuario_id = db.Column(db.Integer,db.ForeignKey('usuario.id'))
    personaje_id = db.Column(db.Integer, nullable=False)

    def __init__ (self, usuario_id, personaje_id):
        self.usuario_id = usuario_id
        self.personaje_id = personaje_id

    def __repr__(self):
        return '<PersonajeFavoritos %r>' % self.personaje_id

    def serialize(self):
        return{
            "personaje_id": self.personaje_id
        }
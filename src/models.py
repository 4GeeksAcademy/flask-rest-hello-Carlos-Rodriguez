from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(120),  nullable=False)
    last_name = db.Column(db.String(120),  nullable=False)
    def __repr__(self):
        return '<User %r>' % self.first_name
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),  nullable=False)
    gender = db.Column(db.Enum('masculine', 'femenine', 'non_binary'),  nullable=False)
    birth_day = db.Column(db.String(50), nullable=False)
    eye_color = db.Column(db.String(50), nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_day": self.birth_day,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "planet_id": self.planet_id
        }
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),  nullable=False)
    climate = db.Column(db.String(50),  nullable=False)
    terrain = db.Column(db.String(50), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Planets %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population
        }
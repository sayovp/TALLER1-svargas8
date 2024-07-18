from db import db

class Guarderia(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(30), nullable=True)
    Direccion = db.Column(db.String(30), nullable=True)
    Telefono = db.Column(db.Integer, nullable=True)

   # cuidadores = db.relationship('Cuidadores', backref="guarderia", lazy=True)
    perros = db.relationship('Perro', backref="guarderia", lazy=True)
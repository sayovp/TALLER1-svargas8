from db import db

class Perro(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(30), nullable=True)
    Raza = db.Column(db.String(30), nullable=True)
    Edad = db.Column(db.Integer, nullable=True)
    Peso = db.Column(db.Float(5,2), nullable=True)
    ID_GUARDERIA = db.Column(db.Integer, db.ForeignKey("guarderia.ID"),nullable=True)
    ID_CUIDADOR = db.Column(db.Integer, db.ForeignKey("cuidadores.ID"),nullable=True)


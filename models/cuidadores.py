from db import db

class Cuidadores(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(45), nullable=True)
    Telefono = db.Column(db.String(45), nullable=True)
    ID_GUARDERIA = db.Column(db.Integer, db.ForeignKey("cuidadores.ID"),nullable=True)

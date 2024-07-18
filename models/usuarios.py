from flask_login import UserMixin
from db import db

class Usuarios(UserMixin , db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreusuario = db.Column(db.String(45), nullable=False)
    contrasena = db.Column(db.String(45), nullable=False)
    es_admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, id, nombreusuario, contrasena, es_admin):
        self.id = id
        self.nombreusuario = nombreusuario
        self.contrasena = contrasena
        self.es_admin = es_admin
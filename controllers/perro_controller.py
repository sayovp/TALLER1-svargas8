from flask import render_template, make_response
from flask_restful import Resource
from flask_login import login_required
from models.perro import Perro
from db import db

class PerroController(Resource):
    
    @login_required
    def get(self):
        perros = Perro.query.filter(Perro.Nombre == 'Lassie').all()
        perrosMario = Perro.query.filter(Perro.ID_CUIDADOR == 1).all()
        #print(current_user)
        return make_response(render_template("perro.html", perros = perros,perrosMario =perrosMario, cantperro = len(perros)))
    
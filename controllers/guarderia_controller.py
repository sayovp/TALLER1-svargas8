from flask import render_template, make_response
from flask_restful import Resource
from flask_login import login_required
from models.guarderia import Guarderia
from db import db

class GuarderiaController(Resource):
    @login_required
    def get(self):
        guarderias = Guarderia.query.all()
        return make_response(render_template("guarderias.html", guarderias=guarderias))

from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Api
from flask_login import LoginManager, login_required, login_user
from dotenv import load_dotenv
from db import db
from controllers.cuidadores_controller import CuidadorController
from controllers.guarderia_controller import GuarderiaController
from controllers.perro_controller import PerroController
from models.usuarios import Usuarios
import os

load_dotenv()

secret_key =  os.urandom(24)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("URL_BD")}/{os.getenv("TABLE_BD")}'
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
api = Api(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(idusuarios):
    usuario = Usuarios.query.get(idusuarios)
    if usuario:
        return usuario
    return None


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        nombreusuario = request.form['nombreusuario']
        contrasena = request.form['contrasena']
        print(nombreusuario)
        user = Usuarios.query.filter_by(nombreusuario = nombreusuario, contrasena = contrasena).first()
        
        if user:
            print(user.nombreusuario)
            print(user.es_admin)
            login_user(user)
            print(user.es_admin)
            if user.es_admin:
                print("entre")
                return redirect(url_for("perrocontroller"))
            else:
                return redirect(url_for("home"))
        
    return render_template("login.html")

api.add_resource(CuidadorController, '/cuidadores')
api.add_resource(PerroController, '/perros')
api.add_resource(GuarderiaController, '/guarderias')

if __name__ == '__main__':
    app.run(debug=True)
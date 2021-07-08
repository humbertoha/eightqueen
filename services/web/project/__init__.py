from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from .models.shared import db
from .models.peticiones import peticiones
from .models.soluciones import soluciones
from .utilslocal import eightqueen
from flask import render_template
from flask import request


app = Flask(__name__)
app.config.from_object("project.config.Config")
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html", num_posts=1)

@app.route('/eight', methods = ['POST'])
def eightroute():
    datarespuesta = {
        "mensaje": "",
        "total" : 0,
        "soluciones" : 0,
        "status" : False
    }
    numerodereina = request.form['numerodereina']
    if(int(numerodereina)>=4):
        respuesta = eightqueen.eightqueen(int(numerodereina))
        datarespuesta["mensaje"] = "Correcto"
        datarespuesta["total"] = len(respuesta.solutions)
        datarespuesta["soluciones"] = respuesta.solutions
        datarespuesta["status"] = True
        count = db.session.query(peticiones).filter(peticiones.numeroreinas == int(numerodereina)).count()
        if(count == 0):
            pet = peticiones(numeroreinas=int(numerodereina),tiempo="No")
            db.session.add(pet)
            db.session.commit()
            for solucion in respuesta.solutions:
                sol = soluciones(numeroreinas=int(numerodereina),solucion=str(solucion))
                db.session.add(sol)
                db.session.commit()
    else:
        datarespuesta["mensaje"] = "Ingresa un numero de reinas(pieza de ajedrez) >= 4"
    return datarespuesta

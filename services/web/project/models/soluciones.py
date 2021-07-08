from .shared import db
from sqlalchemy.ext import mutable




class soluciones(db.Model):
    __tablename__ = "soluciones"
    numerosolucion = db.Column(db.Integer, primary_key=True)
    numeroreinas = db.Column(db.Integer, db.ForeignKey('peticiones.numeroreinas'),nullable=False)
    solucion = db.Column(db.Text, unique=False, nullable=False)
    
    def __init__(self, numeroreinas,solucion):
        self.numeroreinas = numeroreinas
        self.solucion = solucion

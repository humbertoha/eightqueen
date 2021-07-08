from .shared import db


class peticiones(db.Model):
    __tablename__ = "peticiones"

    numeroreinas = db.Column(db.Integer, primary_key=True)
    tiempo = db.Column(db.String(128), unique=False, nullable=False)
    
    def __init__(self, numeroreinas,tiempo):
        self.numeroreinas = numeroreinas
        self.tiempo = tiempo
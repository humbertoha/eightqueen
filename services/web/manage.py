from flask.cli import FlaskGroup
from project import app, db
from project.utilslocal import eightqueen
import pytest
import click
from project.models.peticiones import peticiones
from project.models.soluciones import soluciones


cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("test")
def test():
    pytest.main(['--rootdir', './project/tests'])

@cli.command("cliejecucion")
@click.option('--nq')
def cliqueen(nq):
    nq = int(nq)
    if(nq>=4):
        output = eightqueen.eightqueen(nq)
        print("Tablero :"+nq+" x "+nq+"\nTotal campos:"+(int(nq)*int(nq))+"\n")
        print("numero de reinas(piezas de ajedrez): "+ str(nq)+"\n") 
        print("numero de soluciones: "+ str(len(output.solutions))+"\n")
        count = db.session.query(peticiones).filter(peticiones.numeroreinas == int(nq)).count()
        if(count == 0):
            pet = peticiones(numeroreinas=int(nq),tiempo="No")
            db.session.add(pet)
            db.session.commit()
            for solucion in output.solutions:
                sol = soluciones(numeroreinas=int(nq),solucion=str(solucion))
                db.session.add(sol)
                db.session.commit()
    else:
        print( "Ingresa un numero de reinas(pieza de ajedrez) >= 4")

if __name__ == "__main__":
    cli()
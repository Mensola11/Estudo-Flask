from estudo import app
from flask import render_template , url_for

@app.route("/")
def homepage():
    usuario = "CampCodeBrasil"
    idade = "28 anos"
    
    context = {
        'usuario':usuario,
        'idade':idade
    }
    return render_template('index.html', context=context)

@app.route("/novapag")
def novapag():
    return 'Nova Página'

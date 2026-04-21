from estudo import app
from flask import render_template , url_for, request

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
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa': pesquisa})
    return render_template('Contato.html', context=context)


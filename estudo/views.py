from estudo import app, db
from flask import render_template , url_for, request

from estudo.models import Contato

@app.route("/")
def homepage():
    usuario = "CampCodeBrasil"
    idade = "28 anos"
    
    context = {
        'usuario':usuario,
        'idade':idade
    }
    return render_template('index.html', context=context)

@app.route("/contato/", methods=['GET','POST'])
def novapag():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET', pesquisa)
        context.update({'pesquisa': pesquisa})
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        
        contato = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )
        
        db.session.add(contato)
        db.session.commit()
        
        
    return render_template('Contato.html', context=context)


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from estudo import db, bcrypt
from estudo.models import Contato, User

class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(),EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')
    
    def validate_email(self, email):
        if User.query.filter_by(email = email.data).first():
            return ValidationError('Usuário já cadastrado com esse E-mail!!')
    def save(self):
            senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
            user = User(
                nome = self.nome.data,
                sobrenome = self.sobrenome.data,
                email = self.email.data,
                senha = senha
            )
            
            db.session.add(user)
            db.session.commit()
            return user
        
class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')
    
    def save(self):
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )
        
        db.session.add(contato)
        db.session.commit()
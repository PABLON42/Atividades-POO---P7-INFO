from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), index=True)
    peso = db.Column(db.String(255))
    altura = db.Column(db.String(255))
    classe = db.Column(db.String(255))

    def __init__(self, name, peso, altura, classe):
        self.name = name
        self.peso = peso
        self.altura = altura
        self.classe = classe

    def __repr__(self):
        return '<Nome: {}>'.format(self.name)


db.create_all()


@app.route('/')
def home():
    result = "<h1>Tabelas</h1><br><ul>"
    for table in db.metadata.tables.items():
        result += "<li>%s</li>" % str(table)
    result += "</ul>"
    return result


@app.route('/adc/')
def addPerson():
    result = "<h1>Adição de Usuários</h1><br><ul>"
    login = Person(name='lixo', peso='0kg', altura='10cm', classe='null')
    db.session.add(login)
    db.session.commit()
    result += "<h4>Usuários Adicionados</h4>"
    return result


@app.route('/deletar/<int:id>')
def delPerson(id):
    result = "<h1>Exclusão de Registro</h1><br><ul>"
    Person = Person.query.get(id)
    db.session.delete(Person)
    db.session.commit()
    result += '<p>Usuário -> Id=' + str(Person.id) + ' Excluido!</p>'
    return result


@app.route('/mostrar/<int:id>')
def showPerson(id):
    Person = Person.query.get(id)
    result = "<h1>Consulta a Registro</h1><br><ul>"
    result += "<p> Id=" + str(Person.id) + "</p>"
    result += "<p> Nome=" + Person.name + "</p>"
    result += "<p> Peso=" + Person.peso + "</p>"
    result += "<p> Altura=" + Person.altura + "</p>"
    result += "<p> Classe=" + Person.classe + "</p>"

    return result


@app.route('/listar')
def showPerson():
    Person = Person.query.order_by(Person.id).all()
    result = '<h1>Usuários</h1><br><ul>'
    for Person in Person:
        result += '<p>'
        result += 'Id=' + str(Person.id)
        result += " <br>Nome= " + Person.name
        result += " <br>Peso= " + Person.peso
        result += " <br>Altura= " + Person.altura
        result += " <br>Classe= " + Person.classe
        result += '</p>'
    return result


@app.route('/alterar/<int:id>')
def alterar(id):
    Person = Person.query.get(id)
    Person.altura = '176cm'
    db.session.commit()
    return 'MUDANÇA CONFIRMADA'


if __name__ == '__main__':
    app.run()
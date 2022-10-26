from helpers.database import db


class Cidade_db():


    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
    def __repr__(self):
        return '<Address %r>' % self.nome
       
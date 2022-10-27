from helpers.database import db


from model.pessoa import Pessoa_db

class Aluno_db():

    def __init__(self,nome, instituicaoDeEnsino, curso, matricula):
        self.nome = nome
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula
        
    def __repr__(self):
        return '<Address %r>' % self.instituicaoDeEnsino
      
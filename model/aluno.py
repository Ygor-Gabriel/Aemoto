from helpers.database import db


class Aluno_db():

    def __init__(self, instituicaoDeEnsino, curso, matricula):
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula
    def __repr__(self):
        return '<Address %r>' % self.instituicaoDeEnsino
from helpers.database import db


class InstituicaoDeEnsino_db():
   
    def __init__(self, nome, logradouro, telefone):
        self.nome = nome
        self.logradouro = logradouro
        self.telefone = telefone
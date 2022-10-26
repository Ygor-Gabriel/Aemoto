from helpers.database import db


class Uf_db(db.Model):
   
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        
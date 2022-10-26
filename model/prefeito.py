from helpers.database import db


class Prefeito_db(db.Model):
   
    def __init__(self, nome):
        self.nome = nome
     
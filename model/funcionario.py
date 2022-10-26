from helpers.database import db


class Funcionario_db(db.Model):
 
    def __init__(self, prefeitura, cargo):
        self.prefeitura = prefeitura
        self.cargo = cargo
     
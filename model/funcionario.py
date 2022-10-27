from helpers.database import db


class Funcionario_db():
 
    def __init__(self, prefeitura, cargo):
        self.prefeitura = prefeitura
        self.cargo = cargo
     
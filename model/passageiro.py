from helpers.database import db


class Passageiro_db():

    def __init__(self, nome, cidadeOrigem, cidadeDestino):
        self.nome = nome
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino
       
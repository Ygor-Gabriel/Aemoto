from helpers.database import db


class Rota_db():
 
    def __init__(self, nomeDestino, prefeitura, qtdalunos,veiculo,passageiro,horaSaida,horaChegada):
        self.nomeDestino = nomeDestino
        self.prefeitura = prefeitura
        self.qtdalunos = qtdalunos
        self.veiculo = veiculo
        self.passageiro = passageiro
        self.horaSaida = horaSaida
        self.horaChegada = horaChegada
       
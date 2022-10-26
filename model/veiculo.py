from helpers.database import db


class Veiculo_db(db.Model):

    def __init__(self, cidade,qtdPassageiros, tipoVeiculo, placa):
        self.cidade = cidade
        self.qtdPassageiros = qtdPassageiros
        self.tipoVeiculo = tipoVeiculo
        self.placa = placa
       
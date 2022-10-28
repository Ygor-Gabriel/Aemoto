from model.aluno import Aluno
from model.cidade import Cidade
from model.endereco import Endereco
from model.funcionario import Funcionario
from model.gestorApp import GestorApp
from model.instituicaoDeEnsino import InstituicaoDeEnsino
from model.motorista import Motorista
from model.passageiro import Passageiro
from model.pessoa import Pessoa
from model.prefeito import Prefeito
from model.prefeitura import Prefeitura
from model.rota import Rota
from model.uf import Uf
from model.veiculo import Veiculo



pessoa = Pessoa("Pedro", "23/09/2001", "email@pedrindograu", "00000-0000")
print(pessoa)

aluno = Aluno("Marcos", "22/33/3333", "email@marcos", "00000-0000", "IFPB", "TSI", "2020201232")
print(aluno)

cidade = Cidade("Guarabira", "GBA")
print(cidade)

endereco = Endereco("58 200-000", "32", "Casa", "em frente a prefeitura", "Rua Joca Ataide")
print(endereco)

prefeitura = Prefeitura("Marcia", "email@marcia", "00000-0000", "Marcia")
print(prefeitura)

funcionario = Funcionario(prefeitura, "Almoxarife")
print(funcionario)

veiculo = Veiculo("Guarabira", "31", "Ônibus", "IPF-3342")
print(veiculo)

gestor = GestorApp("Lula", "30/06/1904", "lulindo@email", "00000-0000")
print(gestor)

instituto = InstituicaoDeEnsino("IFPB", "Rua Professor Carlos Leonardo Arcoverde", "00000-0000")
print(instituto)

motorista = Motorista("Estagiando", "Marí", "Motorista de ônibus")
print(motorista)

passageiro = Passageiro(aluno, "Marí", "Guarabira")
print(passageiro)

prefeito = Prefeito("Joao do Bar", "03/07/1988", "Sidney@mail", "95464-9875")
print (prefeito)

rota = Rota("Guarabira", "32", "Marí", "ônibus", "Pedro", "09:00h", "067:00h")
print(rota)

uf = Uf("Paraíba", "PB")
print(uf)
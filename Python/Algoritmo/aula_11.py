 #Atividade 
class Carro:
    
    def __init__(self, cor, modelo, ano, marca, km, rodas):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.km = km
        self.rodas = rodas


cadastro = print('''
    Cadastre um carro: ''')

cor = input("Qual cor do carro você deseja? ")
modelo = input("Qual modelo você deseja? ")
ano = input("Qual ano você deseja? ")
marca = input("Qual marca você deseja? ")
km = input("Quanto km rodados você quer? ")
rodas = input("Qual tipo de rodas você gostaria? ")

carro = Carro (cor, modelo, ano, marca, km, rodas)
print(carro.cor, carro.modelo, carro.ano, carro.marca, carro.km, carro.rodas)

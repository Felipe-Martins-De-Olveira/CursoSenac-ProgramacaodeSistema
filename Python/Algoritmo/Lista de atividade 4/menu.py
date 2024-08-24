
from nivel_muito_facil import muito_facil
from nivel_facil import facil
from nivel_medio import medio
from acimada_da_media import acimada_da_media

while True:
    print("Escolha um número referente a operação ")

    print ("1 - Nível Muito Facíl")
    print ("2 - Nível facíl")
    print ("3 - Nível médio")
    print ("4 - Nivel Acimda da Média")

    lista = input("Escolha umas da opção de 1 ate 4: ")

    if lista == '1':
        muito_facil()

    elif lista == '2':
        facil()

    elif lista == '3':
        medio()

    elif lista == '4': 
        acimada_da_media

    else:
        repeticao = input('''Você digitou um numero errado, deseja tentar novamente? 
                    S ou  N: ''')
        if repeticao == "N": 
            print("Encerramento programa")
            break
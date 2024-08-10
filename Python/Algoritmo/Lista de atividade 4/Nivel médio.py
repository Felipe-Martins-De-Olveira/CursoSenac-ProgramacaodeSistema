#Atividade 1
# for numeros = list range(1, 11)

# nomes = ["Felipe", "Wanderson", "Iara", "Ivanir", "Vanides"]

# ano_nasc = 2004
# ano_atual = 2024
# anos = [ano_nasc, ano_atual]

# print(f"Lista de números de 1 a 10: {numeros}" )
# print(f"Lista com quatro nomes: {nomes}" )
# print(f"Lista com o ano de nascimento e o ano atual: {anos} " )

#Atividade 2
# agiota = ["Brunno", "Felipe", "Wanderson", "Gustavo", "Guilherme"]


# for agiota in agiota:
#     print(agiota)

#Ativdade 3
# soma_impares = 0

# for numero in range(1, 10):
#     if numero % 2 != 0:
#         soma_impares += numero
    
# print(f"O numeros ímpares são {soma_impares}")


#Ativadade 4 
# numeros = list (range(-11, 0))
# print(f"Lista de números decrescente de -10 a 0: {numeros}" )

#atividade 5
# numero = int(input("Digite um numero da tabuada: "))

# print(f"O número escolhido foi: ")
# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")

#Atividade 6
# n1 = [5, 10, 15, 20, 25]
# soma = 0

# try:
   
#     for numero in n1:
#         soma += n1

#     print(f'A soma dos números é: {soma}')

# except:

#     print(f'Ocorreu um na soma:')

#Atividade 7
# def calcular_media(lista):
#     try:
#         media = sum(lista) / len(lista)
#     except:
#         return "A lista está vazia, não é possível calcular a média."
#     return media

# valores = [10, 20, 30, 40, 50]
# print(f"A média dos valores é: {calcular_media(valores)}")

# valores_vazios = []
# print(f"A média dos valores é: {calcular_media(valores_vazios)}")
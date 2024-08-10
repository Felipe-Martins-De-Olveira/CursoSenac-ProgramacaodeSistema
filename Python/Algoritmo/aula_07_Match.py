#Aula
# a = 1 
# match a: 
#     case 1: 
#         print ("Papel")
#     case 2: 
#         print("Pedra")
#     case 3:
#         print ("Tesoura")
#     case _:
#         print("Digite uma opção correta")

# if a == 1:
#     print("Papel")

# elif a == 2:
#     print ("Pedra")

# elif a == 3:
#     print ("Tesoura")

# else: 
#     print("Digite novamente uma opção correta: ")

# def adicao (a, b)
#     soma = a + b
#     print (soma)

#     n1 = 10 
#     n2 = 20

#     adicao()

#Atividade 
def adicao (a1, b2):
    soma = a1 + b2
    return (soma)

def subtracao (n1, n2):
    subtraco = n1 - n2
    return (subtraco)

def multiplicacao (n1, n2):
    multi = n1 * n2
    return (multi)

def divisao (n1, n2):
    divi = n1 / n2
    return (divi)

print("Escolha uma operação")
print("1: Adição")
print("2: Subtracao")
print("3: Multiplicação")
print("4: Divisão")
n1 = float(input("Digite um número: "))
n2 = float(input ("Digite o segundo número: "))
opcao = int(input("Escolha uma opção de Entre 1 ate 4 "))

match opcao: 
    case 1:
        a = adicao(n1, n2)
        print(f"O resultado da conta é: {a}")
    case 2: 
        b = subtracao(n1,n2)
        print(f"O resultado da conta é: {b}")
    case 3: 
       c = multiplicacao (n1, n2)
       print(f"O resultado da conta é: {c}")
    case 4: 
        d = divisao (n1, n2)
        print(f"O resultado da conta é: {d}")
    case _:
        ("Opção invalida")



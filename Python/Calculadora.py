# #Atividade

# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))


# print("Escolha uma operação")
# print("A: Adição")
# print("B: Subtracao")
# print("C: Multiplicação")
# print("D: Divisão")

# operacao = input("")

# if operacao == "A":
#     soma = n1 + n2
#     print(f"O resultado é {soma}")

# elif operacao == "B":
#     subtracao = n1 - n2
#     print (f"O resultado é {subtracao}")

# elif operacao == "C":
#     multiplicacao = n1 * n2
#     print(f"O resultado é {multiplicacao}")

# elif operacao == "D":    
#     divisao = n1 / n2
#     print (f" O resultado é {divisao}")

# else:
#     print ("Operação invalida")

#Correção
print("Calculadora")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))
print("Escolha um número referente a operação ")

print ("1 - Adição")
print ("2 - Subtração")
print ("3 - Divisão")
print ("4 - Multiplicação")
while True:
    operacao = input ("Digite qual operação você deseja: ")
    if operacao == "1":
        resultado = n1 + n2
        break

    elif operacao == "2":
        resultado = n1 - n2
        break

    elif operacao == "3":
        resultado = n1 / n2
        break

    elif operacao == "4":
        resultado = n1 * n2
        break

    else:
        print("Digite um número entre 1 e 4" )

print (f" Resultado da operação: {resultado}")


# Aula

# == Caso seja igual
# n1 > n2: n1 e maior do que n2
# n1 < n2: n1 é menor do que o n2
# n1 != n2 Diferente

# numero_1  =  10
# numero_2 = 20

# if numero_1 > numero_2:
#     print(f'{numero_1} é maior  que {numero_2}')

# else:
#   print(f"{n1} não é maior que {n2}")

# Atividade

# n1 = int(input("Digite o primeiro número:" ))
# n2 = int(input("Digite o segundo número:" ))

# if n1 == n2:
#     print("É igual")

# else:
    # print("Não é igual") 

print("Escolha uma operação")
print("A: Adição")
print("B: Subtracao")
print("C: Multiplicação")
print("D: Divisão")

operacao = input("Digite uma operação A/B/C/D")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if operacao == "A":
    soma = n1 + n2
    print(f"O resultado é {soma}")

elif operacao == "B":
    subtracao = n1 - n2
    print (f"O resultado é {subtracao}")

elif operacao == "C":
    multiplicacao = n1 * n2
    print(f"O resultado é {multiplicacao}")

elif operacao == "D":    
    divisao = n1 / n2
    print (f" O resultado é {divisao}")

else:
    print ("Operação invalida")
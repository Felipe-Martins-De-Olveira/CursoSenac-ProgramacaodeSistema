print("Escolha uma operação")
print("A: Soma")
print("B: Subtracao")
print("C: Multiplicação")
operacao = input("D: Divisão")

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
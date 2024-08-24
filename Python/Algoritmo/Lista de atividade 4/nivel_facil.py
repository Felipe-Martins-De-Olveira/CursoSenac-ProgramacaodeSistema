def facil():
    # Atividade 1
    n1 = int(input("Digite um número: "))

    if n1 % 2 == 0:
        print (f"O numero {n1} é par")

    else:
        print(f"O número {n1} é impar")

    # Atividade 2
    idade = int(input("Digite a sua idade: "))

    if 0 < idade < 12:
        print ("Sua classificação é crinaça")

    elif 12 <= idade <= 18:
        print("Sua classificação é Adolescente")

    elif idade > 18:
        print("Sua classificação é Adulto")

    # Atividade 3
    usuario_c = input("Digite seu nome de usuario: ")
    senha_c = input("Digite sua senha: ")

    usuario = "Felipe"
    senha = "1234"

    if usuario_c == usuario and senha_c == senha:
        print("Usuario encontrado")

    else:
        print("Usuario não encontrado")

    # Atividade 4
    x = float(input("Digite as cordenadas de X: "))
    y = float(input("Digite as cordenadas de y: "))

    if x > 0 and y > 0:
        print("Primeiro quadrante")

    elif x < 0 and y > 0:
        print("Segundo quadrante")

    elif x < 0 and y < 0:
        print ("Terceiro Quadrante")

    elif x > 0 and y < 0:
        print("Quarto quadrante")

    else:
        print("O ponto está localizado no eixo ou origem. ")
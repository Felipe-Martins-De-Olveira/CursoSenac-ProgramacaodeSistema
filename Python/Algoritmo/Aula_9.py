while True:
    letra = input("Escreva algo no teclado")
    try:
        letra = int(letra)
        print ("O caractere digitado é um número: ")
    except:
        print("O Caractere digítado é uma letra")

    repeticao = input('''Deseja tentar com outro caractere? 
                      S ou  N''')
    if repeticao == "N":
        print("Encerramento programa")
        break

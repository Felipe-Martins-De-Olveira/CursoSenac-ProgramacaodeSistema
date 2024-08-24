def acimada_da_media():
    #Atividade 1
     identidade = ["nome",  "idade", "cidade"]
     valores = ["Felipe", 20, "Planaltina-DF"]
     pessoa = dict(zip(identidade, valores))

     print(f"Nome: {pessoa['nome']}")
     print(f"Idade: {pessoa['idade']}")
     print(f"Cidade: {pessoa['cidade']}")

    #Atividade 2
     identidade = ["nome",  "idade", "cidade"]
     valores = ["Felipe", 20, "Planaltina-DF"]
     pessoa = dict(zip(identidade, valores))

     pessoa ["idade"] = 21
     pessoa ["profissao"] = "Desenvolvedor"

     del pessoa ["cidade"]

     print(pessoa)

    #Atividade 3 
     quadrados = {i: i**2 for i in range(1, 6)}

     print(quadrados)

    #atividade 4

     valores = ["Felipe", 21, "Planaltuina-DF", "Desenvolvedor"]

     valor = 21

     if valor in valores:
         print(f"O valor '{valor}' existe na lista.")

     else:
         print(f"O valor '{valor}' não existe na lista")

    #Atividade 5 
     frase = "este é um exemplo de frase com várias palavras e esta frase é um exemplo"

     palavras = frase.lower().split()

     frequencias = {}

     for palavra in palavras:
         if palavra in frequencias:
             frequencias[palavra] += 1
         else:
             frequencias[palavra] = 1

     for palavra, contagem in frequencias.items():
         print(f"'{palavra}': {contagem}")

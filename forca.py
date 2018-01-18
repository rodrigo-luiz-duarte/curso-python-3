import random

def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    enforcou = False
    acertou = False
    letras_acertadas = ["_" for letra in palavra_secreta]
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        
        print("Jogando...")
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        index = 0

        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    print("Encontrei a letra {} na posição {}".format(letra, index))
                    letras_acertadas[index] = letra
                index += 1
                acertou = "_" not in letras_acertadas
        else:
            erros += 1
            enforcou = erros == 6

        print(letras_acertadas)
        

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
    
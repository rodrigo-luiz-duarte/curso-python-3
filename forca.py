import random

def imprime_mensagem_abertura():
    print("***********************************")
    print("*** Bem vindo ao jogo da Forca! ***")
    print("***********************************")

def carrega_palavra_secreta():
    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Você ganhou!")

def imprime_mensagem_perdedor():
    print("Você perdeu!")

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    enforcou = False
    acertou = False
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            
        acertou = "_" not in letras_acertadas
        enforcou = erros == 6

        print(letras_acertadas)
        

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
        
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
    
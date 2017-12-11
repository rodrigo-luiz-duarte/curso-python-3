import random

def jogar():

    print("************************************")
    print(" Bem vindo ao jogo de Adivinhação! *")
    print("************************************")

    # Definição das viaráveis
    valor_minimo_chute = 1
    valor_maximo_chute = 100
    numero_secreto = random.randrange(1,valor_maximo_chute + 1)
    total_de_tentativas = 0
    pontos = 1000
    pontos_perdidos = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre {} e {}: ".format(1,100))
        print("Você digitou:", chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (chute < valor_minimo_chute or chute > valor_maximo_chute):
            print("Você deve informar um número entre {} e {}".format(1,100))
            continue

        if (acertou):
            print("Você acertou e sua pontuação foi {}.".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
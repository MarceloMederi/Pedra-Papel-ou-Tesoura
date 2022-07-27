from random import randint
import time
import os

def apagar():
    os.system("CLS")

def jokenpo():

    def inicio():
        print("=-" * 5)
        print("PEDRA")
        print("=-" * 5)
        time.sleep(1)
        print("PAPEL")
        print("=-" * 5)
        time.sleep(1)
        print("TESOURA")
        print("=-" * 5) 

    def jogo():
        print(" JO...")
        time.sleep(1)
        print(" KEN...")
        time.sleep(1)
        print(" PO...")

    inicio()
    print()

    jogador = int(input("Suas opçoes são?\n"
    "[0- Papel]\n" 
    "[1- Pedra]\n"
    "[2- Tesoura]:"))
    print()

    opcoes = ['Papel', 'Pedra', 'Tesoura']
    adversario = randint(0, 2)

    time.sleep(2)

    jogo()

    print("=-" * 15 )
    print("Voce escolheu {}".format(opcoes[jogador]))
    print("O oponente escolheu {}".format(opcoes[adversario]))
    print("=-" * 15 )

    if jogador == 0: # jogador jogou Papel
        if adversario == 0:
            print("Deu empate. Mais sorte na proxima jogada.")
            print()
        elif adversario == 1:
            print("Você ganhou. Continue nesta onda")
            print()
        elif adversario == 2:
            print("Você perdeu. Que pena não desista.")
            print()
        else:
            print("JOGADA INVALIDA!!!!!")
            print()

    elif jogador == 1: # jogador jogou Pedra
        if adversario == 0:
            print("Você perdeu. Que pena não desista.")
            print()
        elif adversario == 1:
            print("Deu empate. Mais sorte na proxima jogada.")
            print()
        elif adversario == 2:
            print("Você ganhou. Continue nesta onda.")
            print()
        else:
            print("JOGADA INVALIDA!!!!!")
            print()

    elif jogador == 2: # jogador jogou Tesoura
        if adversario == 0:
            print("Você ganhou. Continue nesta onda.")
            print()
        elif adversario == 1:
            print("Você perdeu. Que pena não desista.")
            print()
        elif adversario == 2:
            print("Deu empate. Mais sorte na proxima jogada.")
            print()
        else:
            print("JOGADA INVALIDA!!!!!")
            print()
    else:
        print("FIM DE JOGO!!!!!")
        print()

while True:
    jokenpo()
    apagar()
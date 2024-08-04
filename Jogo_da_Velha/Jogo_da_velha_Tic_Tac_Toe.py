import random
import os

class jogo_da_velha:
    def __init__(self):
        self.tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.termino = ""
    def printar_tabuleiro(self):
        print("")
        print(" " + self.tabuleiro[0][0] + " |" + self.tabuleiro[0][1] + " | " + self.tabuleiro[0][2])
        print(------------)
        print(" " + self.tabuleiro[1][0] + " |" + self.tabuleiro[1][1] + " | " + self.tabuleiro[1][2])
        print(------------)
        print(" " + self.tabuleiro[2][0] + " |" + self.tabuleiro[2][1] + " | " + self.tabuleiro[2][2])

    def resetar_tabuleiro(self):
        pass

    def checar_ganhador(self):
        pass

    def jogada_player(self):
        pass

    def jogada_computador(self):
        pass

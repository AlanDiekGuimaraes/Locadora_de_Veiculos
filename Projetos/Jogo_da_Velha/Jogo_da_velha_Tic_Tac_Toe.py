import random  # Importa a biblioteca random para gerar movimentos aleatórios do computador
import os  # Importa a biblioteca os para limpar a tela do terminal

class jogo_da_velha:
    def __init__(self):
        self.resetar_tabuleiro()  # Inicializa o tabuleiro resetando-o para a configuração inicial

    def printar_tabuleiro(self):
        # Imprime o tabuleiro atual no console
        print("")
        print(" " + self.tabuleiro[0][0] + " | " + self.tabuleiro[0][1] + " | " + self.tabuleiro[0][2])
        print("-----------")
        print(" " + self.tabuleiro[1][0] + " | " + self.tabuleiro[1][1] + " | " + self.tabuleiro[1][2])
        print("-----------")
        print(" " + self.tabuleiro[2][0] + " | " + self.tabuleiro[2][1] + " | " + self.tabuleiro[2][2])

    def resetar_tabuleiro(self):
        # Reseta o tabuleiro para a configuração inicial (vazio)
        self.tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.termino = ""  # Define o status do jogo como não terminado

    def checar_ganhador(self):
        dicionario_ganhador = {}  # Dicionário para armazenar se "X" ou "O" venceram

        for i in ["X", "O"]:
            # Horizontais
            dicionario_ganhador[i] = (self.tabuleiro[0][0] == self.tabuleiro[0][1] == self.tabuleiro[0][2] == i)
            dicionario_ganhador[i] = (self.tabuleiro[1][0] == self.tabuleiro[1][1] == self.tabuleiro[1][2] == i) or dicionario_ganhador[i]
            dicionario_ganhador[i] = (self.tabuleiro[2][0] == self.tabuleiro[2][1] == self.tabuleiro[2][2] == i) or dicionario_ganhador[i]

            # Verticais
            dicionario_ganhador[i] = (self.tabuleiro[0][0] == self.tabuleiro[1][0] == self.tabuleiro[2][0] == i) or dicionario_ganhador[i]
            dicionario_ganhador[i] = (self.tabuleiro[0][1] == self.tabuleiro[1][1] == self.tabuleiro[2][1] == i) or dicionario_ganhador[i]
            dicionario_ganhador[i] = (self.tabuleiro[0][2] == self.tabuleiro[1][2] == self.tabuleiro[2][2] == i) or dicionario_ganhador[i]

            # Diagonais
            dicionario_ganhador[i] = (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == i) or dicionario_ganhador[i]
            dicionario_ganhador[i] = (self.tabuleiro[2][0] == self.tabuleiro[1][1] == self.tabuleiro[0][2] == i) or dicionario_ganhador[i]

        if dicionario_ganhador["X"]:
            self.termino = "x"  # Define o status do jogo como vencido por "X"
            print("X venceu")
            return

        elif dicionario_ganhador["O"]:
            self.termino = "o"  # Define o status do jogo como vencido por "O"
            print("O venceu")
            return

        checador = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] != " ":
                    checador += 1
                    break

        if checador == 0:
            self.termino = "d"  # Define o status do jogo como empate
            print("Empate")
            return

    def jogada_player(self):
        jogada_invalida = True

        while jogada_invalida:
            try:
                print("Digite a linha do seu próximo lance")
                x = int(input())  # Recebe a linha do próximo movimento do jogador

                print("Digite a coluna do seu próximo lance")
                y = int(input())  # Recebe a coluna do próximo movimento do jogador

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print("Coordenadas inválidas")

                if self.tabuleiro[x][y] != " ":
                    print("Posição já preenchida")
                    continue

            except Exception as erro:
                print(erro)
                continue

            jogada_invalida = False
        self.tabuleiro[x][y] = "X"  # Marca o movimento do jogador no tabuleiro

    def jogada_computador(self):
        jogada_computador = []

        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == " ":
                    jogada_computador.append((i, j))

        if len(jogada_computador) > 0:
            x, y = random.choice(jogada_computador)  # Escolhe uma posição aleatória vazia no tabuleiro
            self.tabuleiro[x][y] = "O"  # Marca o movimento do computador no tabuleiro

jogo_da_velha = jogo_da_velha()  # Cria uma instância do jogo
jogo_da_velha.printar_tabuleiro()  # Imprime o tabuleiro inicial
proximo = 0

while proximo == 0:
    os.system("cls")  # Limpa a tela do terminal
    jogo_da_velha.printar_tabuleiro()  # Imprime o tabuleiro atual
    while jogo_da_velha.termino == "":
        jogo_da_velha.jogada_player()  # Jogador faz sua jogada
        jogo_da_velha.jogada_computador()  # Computador faz sua jogada
        os.system("cls")  # Limpa a tela do terminal
        jogo_da_velha.printar_tabuleiro()  # Imprime o tabuleiro atualizado
        jogo_da_velha.checar_ganhador()  # Verifica se há um ganhador

    print("Digite 1 para sair ou qualquer tecla para jogar novamente")
    proximo = input()  # Recebe a entrada do jogador para continuar ou sair do jogo

    if proximo == "1":
        break  # Sai do loop e termina o jogo
    else:
        jogo_da_velha.resetar_tabuleiro()  # Reseta o tabuleiro para uma nova partida
        proximo = 0  # Reinicia o controle do loop para continuar jogando

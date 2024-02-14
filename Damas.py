# inicializa o tabuleiro de damas
def inicializar_tabuleiro():
    tabuleiro = [
        [" ", "X", " ", "X", " ", "X", " ", "X"],
        ["X", " ", "X", " ", "X", " ", "X", " "],
        [" ", "X", " ", "X", " ", "X", " ", "X"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["O", " ", "O", " ", "O", " ", "O", " "],
        [" ", "O", " ", "O", " ", "O", " ", "O"],
        ["O", " ", "O", " ", "O", " ", "O", " "]
    ]
    return tabuleiro

# imprime o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    print("    0   1   2   3   4   5   6   7")
    print("  ---------------------------------")
    for i in range(len(tabuleiro)):
        print(f"{i} | {' | '.join(tabuleiro[i])} |")
        print("  ---------------------------------")

# validação
def validar_movimento(origem, destino, jogador, tabuleiro):
    if not (0 <= origem[0] < 8 and 0 <= origem[1] < 8):
        return False
    if not (0 <= destino[0] < 8 and 0 <= destino[1] < 8):
        return False
    if tabuleiro[origem[0]][origem[1]] != jogador:
        return False
    if tabuleiro[destino[0]][destino[1]] != " ":
        return False
    if abs(destino[0] - origem[0]) == 1 and abs(destino[1] - origem[1]) == 1:
        return True
    if abs(destino[0] - origem[0]) == 2 and abs(destino[1] - origem[1]) == 2:
        meio_x = (destino[0] + origem[0]) // 2
        meio_y = (destino[1] + origem[1]) // 2
        if tabuleiro[meio_x][meio_y] != " " and tabuleiro[meio_x][meio_y] != jogador:
            return True
    return False

# realiza um movimento
def realizar_movimento(origem, destino, tabuleiro):
    tabuleiro[destino[0]][destino[1]] = tabuleiro[origem[0]][origem[1]]
    tabuleiro[origem[0]][origem[1]] = " "

    if abs(destino[0] - origem[0]) == 2:
        meio_x = (destino[0] + origem[0]) // 2
        meio_y = (destino[1] + origem[1]) // 2
        tabuleiro[meio_x][meio_y] = " "

# main
def main():
    jogador_atual = "X"
    tabuleiro = inicializar_tabuleiro()
    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        origem = tuple(map(int, input("Digite a posição da peça que deseja mover (linha coluna): ").split()))
        destino = tuple(map(int, input("Digite a posição para onde deseja mover a peça (linha coluna): ").split()))
        if validar_movimento(origem, destino, jogador_atual, tabuleiro):
            realizar_movimento(origem, destino, tabuleiro)
            if jogador_atual == "X":
                jogador_atual = "O"
            else:
                jogador_atual = "X"
        else:
            print("Movimento inválido. Tente novamente.")

if __name__ == "__main__":
    main()

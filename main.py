import numpy as np
# 9x9 sudoku puzzle
Sudoku = [[4, 0, 9, 7, 0, 0, 0, 3, 2],
          [2, 8, 1, 6, 9, 0, 0, 0, 5],
          [7, 3, 0, 4, 8, 2, 0, 0, 6],
          [0, 0, 0, 2, 7, 0, 9, 0, 0],
          [0, 0, 0, 0, 0, 8, 2, 0, 0],
          [0, 0, 2, 0, 0, 5, 6, 1, 3],
          [9, 0, 0, 0, 1, 0, 3, 7, 8],
          [1, 5, 0, 3, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 9, 5, 6, 0], ]

# Função que filtra as 3 possibilidades para alteração de uma célula
def possibilidade(linha, coluna, num):
    global Sudoku
    for i in range(0, 9):
        if Sudoku[linha][i] == num:
            return False

    for i in range(0, 9):
        if Sudoku[i][coluna] == num:
            return False

    x0 = (coluna // 3) * 3
    y0 = (linha // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if Sudoku[y0 + i][x0 + j] == num:
                return False

    return True

# Chama a função possibilidade()  sempre que tiver u numero com valor = 0 dentro do grid
# caso a função possibilidade() retorne = True, substitui o numero 0 por um numero entre 1 - 9.
def solucao():
    global Sudoku
    for linha in range(0, 9):
        for coluna in range(0, 9):
            if Sudoku[linha][coluna] == 0:
                for num in range(1, 10):
                    if possibilidade(linha, coluna, num):
                        Sudoku[linha][coluna] = num
                        solucao()
                        Sudoku[linha][coluna] = 0

                return

    print(np.matrix(Sudoku))


solucao()

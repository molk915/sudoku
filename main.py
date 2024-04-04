def znajdz_puste_pole(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j  # wiersz, kolumna
    return None

def czy_mozna_wstawic(sudoku, num, poz):
    # Sprawdzenie wiersza
    for i in range(9):
        if sudoku[poz[0]][i] == num and poz[1] != i:
            return False

    # Sprawdzenie kolumny
    for i in range(9):
        if sudoku[i][poz[1]] == num and poz[0] != i:
            return False

    # Sprawdzenie bloku
    blok_x = poz[1] // 3
    blok_y = poz[0] // 3

    for i in range(blok_y*3, blok_y*3 + 3):
        for j in range(blok_x*3, blok_x*3 + 3):
            if sudoku[i][j] == num and (i,j) != poz:
                return False

    return True

def rozwiaz_sudoku(sudoku):
    znajdz = znajdz_puste_pole(sudoku)
    if not znajdz:
        return True
    else:
        wiersz, kolumna = znajdz

    for i in range(1, 10):
        if czy_mozna_wstawic(sudoku, i, (wiersz, kolumna)):
            sudoku[wiersz][kolumna] = i

            if rozwiaz_sudoku(sudoku):
                return True

            sudoku[wiersz][kolumna] = 0

    return False

sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
# sudoku = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]
# sudoku = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

if rozwiaz_sudoku(sudoku):
    for wiersz in sudoku:
        print(wiersz)
else:
    print("Nie znaleziono rozwiązania")
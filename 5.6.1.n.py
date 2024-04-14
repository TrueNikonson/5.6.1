def front_matrix():
    print("    0    1    2  ")
    for i, j in enumerate(back_matrix):
        j=str(j)
        str_j = f"{i} {j}"
        print(str_j)


def admin():
    while True:
        x = input("Введите координаты:")
        if len(x) != 2:
            print("Введите 2 координаты!")
        a, b = x
        a, b = int(a), int(b)
        if 0 > a or 0 > b or 2 < a or 2 < b:
            print("Координаты вне диапазона!")
        if back_matrix[a][b] != "-":
            print("Клетка занята!")
        return a,b


def win():
    win_comb = (((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)))
    for i in win_comb:
        coords = []
        for coord12 in i:
            coords.append(back_matrix[coord12[0]][coord12[1]])
        if coords == ["X", "X", "X"]:
            print("Выиграл игрок 1!")
            return True
        if coords == ["0", "0", "0"]:
            print("Выиграл игрок 2!")
            return True
    return False


print("Введите числовые координаты хода.")
back_matrix = [["-"] * 3 for i in range(3)]
rounds = 0
while True:
    rounds += 1
    front_matrix()
    if rounds % 2 == 1:
        print(" Ходит игрок 1:")
    else:
        print(" Ходит игрок 2:")
    a, b = admin()
    if rounds % 2 == 1:
        back_matrix[a][b] = "X"
    else:
        back_matrix[a][b] = "0"
    if win():
        break
    if rounds == 9:
        print(" Ничья!")
        break
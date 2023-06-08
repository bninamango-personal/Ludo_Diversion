import random

board = [
    ["20", "META"],
    ["19", " "],
    ["18", " "],
    ["17", " "],
    ["16", " "],
    ["15", " "],
    ["14", "BONUS"],
    ["13", " "],
    ["12", " "],
    ["11", " "],
    ["10", " "],
    ["09", " "],
    ["08", "BONUS"],
    ["07", " "],
    ["06", " "],
    ["05", " "],
    ["04", " "],
    ["03", " "],
    ["02", " "],
    ["01", " "],
    ["INICIO", " "]]


def RenderBoard():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()


def GetValue(x: int, y: int) -> str:
    return board[y][x]


# Logica del player
p1_name = ""
p1_x = p1_y = 0

p2_name = ""
p2_x = p2_y = 0


def InitializePlayer(x: int, y: int, p1: str, p2: str):
    global p1_name, p1_x, p1_y
    global p2_name, p2_x, p2_y
    p1_x = p2_x = x
    p1_y = p2_y = y
    p1_name = p1
    p2_name = p2
    board[p1_y][p1_x] = f"{p1_name} {p2_name}"


# def GetValue(x: int, y: int) -> str:
#     global position_x, position_y
#     position_x = x
#     position_y = y
#     return board[position_y][position_x]


def MovePlayer_P1(y: int):
    global p1_x, p1_y
    board[p1_y][p1_x] = ' '
    p1_y -= y
    if board[p1_y][p1_x] == "BONUS":
        print("¡P1 cayo en BONUS! ,Vuelve a lanzar el dado.")
        force= Launch(input("Ingresa la fuerza de lanzamiento 7w7"))
        p1_y -= (force)
    board[p1_y][p1_x] = p1_name


def MovePlayer_P2(y: int):
    global p2_x, p2_y
    board[p2_y][p2_x] = ' '
    p2_y -= y
    if board[p2_y][p2_x] == "BONUS":
        print("¡P2 cayo en BONUS! Vuelve a lanzar el dado.")
        force =Launch(input("Ingresa fuerza de lanzamiento 0-0"))
        p2_y -=(force)
    board[p2_y][p2_x] = p2_name


def UpdatePlayer():
    # if y < 0:
    #     y = abs(y) - 1
    # board[y][x] = c
    global p1_x, p1_y, p1_name
    global p2_x, p2_y, p2_name
    global turn

    if turn % 2 == 0:
        if p1_y < 0:
            p1_y = abs(p1_y) - 1
    else:
        if p2_y < 0:
            p2_y = abs(p2_y) - 1

    board[p1_y][p1_x] = p1_name
    board[p2_y][p2_x] = p2_name

    # if
    # global position_x, position_y, p1_name, p2_name
    # player = ""
    # if turn % 2 == 0:
    #     player = p1_name
    # else:
    #     player = p2_name
    # if position_y < 0:
    #     position_y = abs(position_y) - 1
    # board[position_y][position_x] = player


# Dado
def Launch(result: str) -> str:
    result = result.lower()
    if result == "debil":
        return random.randint(1, 3)
    elif result == "normal":
        return random.randint(1, 6)
    elif result == "fuerte":
        return random.randint(4, 6)
    elif result == 'one':
        return 1
    return 0


# Game Loop
isGameOver: bool = False
turn = force = 0


def Start():
    InitializePlayer(1, 20, 'P1', 'P2')
    RenderBoard()


def Input():
    global turn, force

    if turn % 2 == 0:
        print("# Turno del jugador 1 #")
    else:
        print("# Turno del jugador 2 #")

    force = Launch(input("Ingrese el tipo de tiro que desea realizar: "))
    print(f"DADO: Obtuvo el valor de {force}")


def Update():
    global turn, force

    if turn % 2 == 0:
        MovePlayer_P1(force)
    else:
        MovePlayer_P2(force)

    UpdatePlayer()


def Render():
    RenderBoard()


Start()
while not isGameOver:
    Input()
    Update()
    Render()
    turn += 1

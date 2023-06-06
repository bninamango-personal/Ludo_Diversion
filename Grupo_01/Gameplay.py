# Logica del tablero
import random

board = []
width = height = 0


def InitializeBoard(w: int, h: int):
    global width, height
    width = w
    height = h
    for i in range(width):
        board.append([' '] * height)
        for j in range(height):
            if j == 0:
                board[i][j] = str(i + 1)


def UpdateBoard():
    for i in range(width):
        for j in range(height):
            if j == 0:
                board[i][j] = str(i + 1)
            else:
                board[i][j] = ' '


def RenderBoard():
    for i in range(width):
        for j in range(height):
            print(board[i][j], end=" ")
        print()


def GetValue(x: int, y: int) -> str:
    return board[y][x]


# Logica del player
position_x = position_y = 0
name = ""


def InitializePlayer(x: int, y: int, c: str):
    global position_x, position_y, name
    position_x = x
    position_y = y
    name = c
    board[position_y][position_x] = name


def MovePlayer(y: int):
    global position_y
    position_y -= y


def GetValue(y: int) -> str:
    global position_y
    position_y = y
    return board[position_y][position_x]


def UpdatePlayer():
    global position_x, position_y, name
    if position_y < 0:
        position_y = abs(position_y) - 1
    board[position_y][position_x] = name


# Dado
def Launch(steps: str) -> str:
    steps = steps.lower()
    if steps == "debil":
        return random.randint(1, 3)
    elif steps == "normal":
        return random.randint(1, 6)
    elif steps == "fuerte":
        return random.randint(4, 6)
    return 0


# Game Loop
force: int = 0
isGameOver: bool = False


def Start():
    InitializeBoard(20, 2)
    InitializePlayer(1, 19, 'Bryan')
    RenderBoard()


def Input():
    global force
    force = Launch(input("Current force: "))


def Update():
    MovePlayer(force)
    UpdateBoard()
    UpdatePlayer()


def Render():
    RenderBoard()


Start()
while not isGameOver:
    Input()
    Update()
    Render()

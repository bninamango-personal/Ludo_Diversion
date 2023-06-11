width = height = 0
board = []


def Create(w: int, h: int):
    global width, height, board
    width = w
    height = h
    for i in range(width):
        board.append(["-"] * height)

    print(f"Lenght: {len(board)}")


def Update(x: int, y: int, c: str) -> object:
    global board


def Render():
    global board
    for i in range(width):
        for j in range(height):
            print(board[i][j], end=" ")
        print()


def CanMove(x: int, y: int, c: str) -> bool:
    global board
    return board[x][y] == c


def Replace(x: int, y: int):
    global board
    board[x][y] = " "


def GetValue(x: int, y: int) -> str:
    global board
    return board[x][y]

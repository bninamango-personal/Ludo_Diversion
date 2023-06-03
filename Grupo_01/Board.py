board = []
width = 0
height = 0


def Create(w: int, h: int):
    width = w
    height = h
    for i in range(width):
        board.append([0] * height)


def Render():
    for i in range(width):
        for j in range(height):
            print(board[i][j], end=" ")
        print(" ")


Create(5, 5)
Render()
board = []
left = 0
right = 0


def Create(l: int, r: int):
    global board,left,right
    left = l
    right = r
    for i in range(left):
        board.append([0] * right)


def Render():
    for i in range(left):
        for j in range(right):
            print(board[i][j], end=" ")
        print(" ")


Create(20, 2)
Render()

def Getvalue(x,y):
    if player1(y)=player2(y)
# # Logica del tablero
# import random
#
# board = [
#     ["20", "META"],
#     ["19", " "],
#     ["18", " "],
#     ["17", " "],
#     ["16", " "],
#     ["15", " "],
#     ["14", "BONUS"],
#     ["13", " "],
#     ["12", " "],
#     ["11", " "],
#     ["10", " "],
#     ["09", " "],
#     ["08", "BONUS"],
#     ["07", " "],
#     ["06", " "],
#     ["05", " "],
#     ["04", " "],
#     ["03", " "],
#     ["02", " "],
#     ["01", " "],
#     ["INICIO", " "]]
#
#
# def RenderBoard():
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             print(board[i][j], end=" ")
#         print()
#
#
# def GetValue(x: int, y: int) -> str:
#     return board[y][x]
#
#
# # Logica del player
# p1_name = ""
# p1_x = p1_y = 0
#
# p2_name = ""
# p2_x = p2_y = 0
#
#
# def InitializePlayer(x: int, y: int, p1: str, p2: str):
#     global p1_name, p1_x, p1_y
#     global p2_name, p2_x, p2_y
#     p1_x = p2_x = x
#     p1_y = p2_y = y
#     p1_name = p1
#     p2_name = p2
#     board[p1_y][p1_x] = f"{p1_name} {p2_name}"
#
#
# # def GetValue(x: int, y: int) -> str:
# #     global position_x, position_y
# #     position_x = x
# #     position_y = y
# #     return board[position_y][position_x]
#
#
# def MovePlayer_P1(y: int):
#     global p1_x, p1_y
#     board[p1_y][p1_x] = ' '
#     p1_y -= y
#
#
# def MovePlayer_P2(y: int):
#     global p2_x, p2_y
#     board[p2_y][p2_x] = ' '
#     p2_y -= y
#
#
# def UpdatePlayer():
#     # if y < 0:
#     #     y = abs(y) - 1
#     # board[y][x] = c
#     global p1_x, p1_y, p1_name
#     global p2_x, p2_y, p2_name
#     global turn
#
#     if turn % 2 == 0:
#         if p1_y < 0:
#             p1_y = abs(p1_y) - 1
#     else:
#         if p2_y < 0:
#             p2_y = abs(p2_y) - 1
#
#     board[p1_y][p1_x] = p1_name
#     board[p2_y][p2_x] = p2_name
#
#
#
#
# # Dado
# def Launch(result: str) -> str:
#     result = result.lower()
#     if result == "debil":
#         return random.randint(1, 3)
#     elif result == "normal":
#         return random.randint(1, 6)
#     elif result == "fuerte":
#         return random.randint(4, 6)
#     elif result == 'one':
#         return 1
#     return 0
#
#
# # Game Loop
# isGameOver: bool = False
# turn = force = 0
#
#
# def Start():
#     InitializePlayer(1, 20, 'Bryan', 'Bryannsss')
#     RenderBoard()
#
#
# def Input():
#     global turn, force
#
#     if turn % 2 == 0:
#         print("# Turno del jugador 1 #")
#     else:
#         print("# Turno del jugador 2 #")
#
#     force = Launch(input("Ingrese el tipo de tiro que desea realizar: "))
#     print(f"DADO: Obtuvo el valor de {force}")
#
#
# def Update():
#     global turn, force
#
#     if turn % 2 == 0:
#         MovePlayer_P1(force)
#     else:
#         MovePlayer_P2(force)
#
#     UpdatePlayer()
#
#
# def Render():
#     RenderBoard()
#
#
# Start()
# while not isGameOver:
#     Input()
#     Update()
#     Render()
#     turn += 1

# -----------------------------------------------------------------------
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
game_over = False
current_turn = 0
dice = 0
p1 = ["name", [0, 0]]
p2 = ["name", [0, 0]]


def Jump_Line(jumps: int):
    print("\n" * (jumps - 1))


def Player1_GetName() -> str:
    return p1[0]


def Player1_GetX() -> int:
    return p1[1][0]


def Player1_GetY() -> int:
    return p1[1][1]


def Player1_SetX(x: int):
    p1[1][0] = x


def Player1_SetY(y: int):
    p1[1][1] = y


def Player2_GetName() -> str:
    return p2[0]


def Player2_GetX() -> int:
    return p2[1][0]


def Player2_GetY() -> int:
    return p2[1][1]


def Player2_SetX(x: int):
    p2[1][0] = x


def Player2_SetY(y: int):
    p2[1][1] = y


def Start():
    p1[1] = [1, 20]
    p2[1] = [1, 20]

    print("##  Jugadores  ##")
    p1[0] = input("Ingrese el nombre del jugador 1: ")
    p2[0] = input("Ingrese el nombre del jugador 2: ")
    print("#" * 20)

    Jump_Line(1)
    Render()


def Input():
    def Get_Dice(launch: str) -> str:
        launch = launch.lower()
        if launch == "debil":
            return random.randint(1, 3)
        elif launch == "normal":
            return random.randint(1, 6)
        elif launch == "fuerte":
            return random.randint(4, 6)
        elif launch == "six":
            return 6
        elif launch == "one":
            return 1
        return 0

    global dice
    print(f"# Turno del jugador {(current_turn % 2) + 1} #")
    dice = Get_Dice(input(f"Ingrese el tipo de tiro que desea realizar: "))
    print(f"DADO: Obtuvo el valor de {dice}")
    Jump_Line(1)


def Update():
    def Get_Value(x: int, y: int) -> str:
        return board[y][x]

    def Lucky():
        global dice, current_turn
        if dice == 6 or (Get_Value(Player1_GetX(), Player1_GetY()) == "BONUS" or Get_Value(Player2_GetX(), Player2_GetY()) == "BONUS"):
            current_turn += 1

    def Move(steps: int):
        board[Player1_GetY()][Player1_GetX()] = ' '
        board[Player2_GetY()][Player2_GetX()] = ' '

        if current_turn % 2 == 0:
            py = Player1_GetY() - steps
            Player1_SetY(py)
        else:
            py = Player2_GetY() - steps
            Player2_SetY(py)

    # def Death():
    #     if current_turn % 2 == 0:
    #

    Move(dice)
    Lucky()


def Render():
    def Draw_Board():
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], end=" ")
            print()

    def Draw_Players():
        board[Player1_GetY()][Player1_GetX()] = Player1_GetName()
        board[Player2_GetY()][Player2_GetX()] = Player2_GetName()

    print("## JUEGO ##")
    print("# Ludo divertido #")
    Draw_Players()
    Draw_Board()

# ---------------------------
if __name__ == '__main__':
    Start()
    while not game_over:
        Input()
        Update()
        Render()
        current_turn += 1

import random
import time

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
p1 = ["p1_name", [0, 0]]
p2 = ["CPU", [0, 0]]
px_aux = py_aux = 0


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


def Player1_ResetPosition():
    p1[1] = [1, 20]


def Player2_ResetPosition():
    p2[1] = [1, 20]


def Get_Value(x: int, y: int) -> str:
    return board[y][x]


def Start():
    p1[1] = [1, 20]
    p2[1] = [1, 20]

    print("##  Jugadores  ##")
    p1[0] = input("Ingrese el nombre del jugador 1: ")
    print("#" * 20)

    Jump_Line(1)
    board[20][1] = f"{Player1_GetName()} {Player2_GetName()}"
    Render(on_start=True)


def Input():
    Jump_Line(1)

    def Get_Dice(launch: str, is_tester: bool = False) -> int:
        launch = launch.lower()
        if launch == "debil":
            return random.randint(1, 3)
        elif launch == "normal":
            return random.randint(1, 6)
        elif launch == "fuerte":
            return random.randint(4, 6)

        if is_tester and launch.isnumeric():
            value = int(launch)
            if 0 < int(value) < 10:
                return value
        return 0

    def Get_Random_Dice() -> int:
        launch = random.randint(1, 3)
        if launch == 1:
            return random.randint(1, 3)
        elif launch == 2:
            return random.randint(1, 6)
        elif launch == 3:
            return random.randint(4, 6)

    global dice
    print(f"# Turno del jugador {(current_turn % 2) + 1} #")

    if current_turn % 2 == 0:
        dice = Get_Dice(input(f"Ingrese el tipo de tiro que desea realizar: "), is_tester=True)

        while dice == 0:
            dice = Get_Dice(input(f"Ingrese un tipo de tiro VALIDO que desea realizar: "), is_tester=True)
    else:
        time.sleep(random.randint(2, 5))
        dice = Get_Random_Dice()

    print(f"DADO: Obtuvo el valor de {dice}")
    Jump_Line(1)


def Update():
    global dice

    def Set_Positions():
        global current_turn, px_aux, py_aux
        px_aux = Player1_GetX() if current_turn % 2 == 0 else Player2_GetX()
        py_aux = Player1_GetY() if current_turn % 2 == 0 else Player2_GetY()

    def Move_Player(steps: int):
        global px_aux, py_aux
        board[py_aux][px_aux] = ' '

        if current_turn % 2 == 0:
            Player1_SetY(abs(py_aux - steps))
            px_aux = Player1_GetX()
            py_aux = Player1_GetY()
        else:
            Player2_SetY(abs(py_aux - steps))
            px_aux = Player2_GetX()
            py_aux = Player2_GetY()

    def Lucky_Player():
        global dice, current_turn
        if dice == 6 or Get_Value(px_aux, py_aux) == "BONUS":
            current_turn += 1

    def Kill_Player():
        global px_aux, py_aux, current_turn
        enemy = Player2_GetName() if current_turn % 2 == 0 else Player1_GetName()

        if Get_Value(px_aux, py_aux) == enemy:
            if current_turn % 2 == 0:
                Player2_ResetPosition()
            else:
                Player1_ResetPosition()

    def Add_Record(data: str):
        write_file = open("Records/Record.txt", 'a')
        read_file = open("Records/Record.txt", 'r')

        index = sum(1 for line in read_file)

        write_file.write(f"[{index + 1}] [{time.ctime(time.time())}] {data}\n")
        write_file.close()

    def Win_Player():
        global current_turn, px_aux, py_aux, game_over

        if Get_Value(px_aux, py_aux) == "META":
            # p_name = Player1_GetName() if current_turn % 2 == 0 else Player2_GetName()

            if current_turn % 2 == 0:
                Add_Record(data=f"{Player1_GetName()}")

            game_over = True

    Set_Positions()
    Move_Player(dice)
    Kill_Player()
    Win_Player()
    Lucky_Player()


def Render(on_start: bool = False):
    def Draw_Board():
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], end=" ")
            print()

    def Draw_Players():
        if on_start:
            return
        board[Player1_GetY()][Player1_GetX()] = Player1_GetName()
        board[Player2_GetY()][Player2_GetX()] = Player2_GetName()

    print("## JUEGO ##")
    print("# Ludo divertido #")
    Draw_Players()
    Draw_Board()


def Game_Loop():
    global board, game_over, current_turn, dice
    global p1, p2, px_aux, py_aux
    Start()
    while not game_over:
        Input()
        Update()
        Render()
        current_turn += 1

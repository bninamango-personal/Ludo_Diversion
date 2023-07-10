import random
import sys
import time
import datetime
from colorama import Back, Fore, init
import Sound as sound_manager
import Info as info_manager
import os

board = [
    [f"{Back.MAGENTA}20 ", "META"],
    ["19 ", " "],
    ["18 ", " "],
    ["17 ", " "],
    ["16 ", " "],
    ["15 ", " "],
    [f"{Back.MAGENTA}14 ", "BONUS"],
    ["13 ", " "],
    ["12 ", " "],
    ["11 ", " "],
    ["10 ", " "],
    ["09 ", " "],
    [f"{Back.MAGENTA}08 ", "BONUS"],
    ["07 ", " "],
    ["06 ", " "],
    ["05 ", " "],
    ["04 ", " "],
    ["03 ", " "],
    ["02 ", " "],
    ["01 ", " "],
    [f"{Back.MAGENTA}INICIO ", " "]]
game_over = False
current_turn = 0
dice = 0
p1 = ["p1_name", [0, 0]]
p2 = ["p2_name", [0, 0]]
px_aux = py_aux = 0
is_pvp = False
winner = "winner"
start_time = final_time = 0

# Part - 2
player_info = dict()
ID = ""
movements = ""


def Jump_Line(jumps: int):
    print("\n" * (jumps - 1))


def Player1_GetName(color: bool = True) -> str:
    return Fore.RED + p1[0] if color else p1[0]


def Player1_GetX() -> int:
    return p1[1][0]


def Player1_GetY() -> int:
    return p1[1][1]


def Player1_SetX(x: int):
    p1[1][0] = x


def Player1_SetY(y: int):
    p1[1][1] = y


def Player2_GetName(color: bool = True) -> str:
    return Fore.BLUE + p2[0] if color else p2[0]


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


# Part - 2
def Player_Register():
    global player_info, ID
    print(f"{Fore.GREEN}## REGISTRO DE JUGADOR ##")

    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    fecha = input("Ingrese su fecha: ")

    player_info = {correo: {"Nombre": nombre, "Fecha": fecha, "Movimientos": "", "Copas": 0}}

    ID = correo
    p1[0] = nombre

    print("####################")


# def Start():
#     global is_pvp, start_time
#
#     Jump_Line(1)
#
#     print(f"{Fore.GREEN}##  Jugadores  ##")
#     p1[0] = input(f"{Fore.RED}Ingrese el nombre del jugador 1: ")
#     p2[0] = input(f"{Fore.BLUE}Ingrese el nombre del jugador 2: ") if is_pvp else "CPU"
#
#     sound_manager.Initialize()
#     sound_manager.StopAll()
#     sound_manager.Play("Theme_gameplay.mp3", 1, volume=0.20, loop=True)
#
#     Player1_ResetPosition()
#     Player2_ResetPosition()
#
#     print(f"{Fore.GREEN}#" * 20)
#
#     Jump_Line(1)
#     board[20][1] = f"{Fore.RED + Player1_GetName()} {Fore.BLUE + Player2_GetName()}"
#     Render(on_start=True)
#     start_time = time.time()

def Reset():
    global board, game_over, current_turn, dice
    global px_aux, py_aux
    global is_pvp, winner
    global movements
    board = [
        [f"{Back.MAGENTA}20 ", "META"],
        ["19 ", " "],
        ["18 ", " "],
        ["17 ", " "],
        ["16 ", " "],
        ["15 ", " "],
        [f"{Back.MAGENTA}14 ", "BONUS"],
        ["13 ", " "],
        ["12 ", " "],
        ["11 ", " "],
        ["10 ", " "],
        ["09 ", " "],
        [f"{Back.MAGENTA}08 ", "BONUS"],
        ["07 ", " "],
        ["06 ", " "],
        ["05 ", " "],
        ["04 ", " "],
        ["03 ", " "],
        ["02 ", " "],
        ["01 ", " "],
        [f"{Back.MAGENTA}INICIO ", " "]]
    current_turn = 0
    game_over = False
    dice = 0
    px_aux = py_aux = 0
    is_pvp = False
    winner = "winner"
    movements = ""

    sound_manager.Initialize()
    sound_manager.StopAll()
    sound_manager.Play("Theme_gameplay.mp3", 1, volume=0.20, loop=True)

    Player1_ResetPosition()
    Player2_ResetPosition()

    print(f"{Fore.GREEN}#" * 20)

    Jump_Line(1)
    board[20][1] = f"{Fore.RED + Player1_GetName()} {Fore.BLUE + Player2_GetName()}"
    Render(on_start=True)


def Start_1():
    global is_pvp, start_time, player_info

    Player_Register()

    Jump_Line(1)

    print(f"{Fore.GREEN}##  ¡Bienvenido {p1[0]}!  ##")

    print(f"¡Comienza el juego{Fore.CYAN} PV1 vs CPU!")

    p2[0] = "CPU"

    sound_manager.Initialize()
    sound_manager.StopAll()
    sound_manager.Play("Theme_gameplay.mp3", 1, volume=0.20, loop=True)

    Player1_ResetPosition()
    Player2_ResetPosition()

    print(f"{Fore.GREEN}#" * 20)

    Jump_Line(1)
    board[20][1] = f"{Fore.RED + Player1_GetName()} {Fore.BLUE + Player2_GetName()}"
    Render(on_start=True)
    start_time = time.time()


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
        return random.randint(4, 6)

    def Type_Gameplay():
        global dice, current_turn, is_pvp, movements

        color = Fore.RED if current_turn % 2 == 0 else Fore.BLUE

        print(f"{color}# Turno del jugador {(current_turn % 2) + 1} #")

        if is_pvp:
            dice = Get_Dice(input(f"{color}Ingrese el tipo de tiro que desea realizar: "), is_tester=True)
            while dice == 0:
                sound_manager.Play("Error.wav", 0)

                dice = Get_Dice(input(f"{color}Ingrese un tipo de tiro VALIDO que desea realizar: "), is_tester=True)
        else:
            if current_turn % 2 == 0:
                dice = Get_Dice(input(f"{color}Ingrese el tipo de tiro que desea realizar: "), is_tester=True)
                movements += f"{dice}-"
                while dice == 0:
                    sound_manager.Play("Error.wav", 0)

                    dice = Get_Dice(input(f"{color}Ingrese un tipo de tiro VALIDO que desea realizar: "),
                                    is_tester=True)
            else:
                time.sleep(random.randint(2, 5))
                dice = Get_Random_Dice()

        print(f"{color}DADO: Obtuvo el valor de {dice}")

    Type_Gameplay()

    sound_manager.Play("Move.wav", 0)

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
            sound_manager.Play("Lucky.wav", 0)
            current_turn += 1

    def Kill_Player():
        global px_aux, py_aux, current_turn
        enemy = Player2_GetName() if current_turn % 2 == 0 else Player1_GetName()

        if Get_Value(px_aux, py_aux) == enemy:
            if current_turn % 2 == 0:
                Player2_ResetPosition()
            else:
                Player1_ResetPosition()
            sound_manager.Play("Death.wav", 0)

    # def Add_Record(data: str):
    #     global start_time, final_time
    #
    #     final_time = time.time()
    #
    #     write_file = open("Data/Record.txt", 'a')
    #     read_file = open("Data/Record.txt", 'r')
    #
    #     index = sum(1 for line in read_file)
    #     read_file.close()
    #
    #     date = time.ctime(final_time)
    #     seconds = final_time - start_time
    #     chronometer = datetime.timedelta(seconds=seconds)
    #
    #     write_file.write(f"[{index + 1}] [{date}] [{chronometer}] {data}\n")
    #     write_file.close()

    def Win_Player():
        global current_turn, is_pvp, winner
        global px_aux, py_aux, game_over
        global player_info, ID, movements

        if Get_Value(px_aux, py_aux) == "META":
            winner = Player1_GetName() if current_turn % 2 == 0 else Player2_GetName()

            if not is_pvp and current_turn % 2 == 0:
                if info_manager.Get_Player(ID) != -1:
                    aux_copas: int = info_manager.Get_Player(ID)["Copas"]

                    player_info[ID].update({"Copas": f"{aux_copas + 1}"})
                else:
                    player_info[ID].update({"Copas": f"{1}"})

                player_info[ID].update({"Movimientos": f"{movements[:-1]}"})

                info_manager.Write_File(player_info)

                # Add_Record(Player1_GetName(color=False))

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
                print(board[i][j], end="")
            print()

    def Draw_Players():
        if on_start:
            return
        board[Player1_GetY()][Player1_GetX()] = Player1_GetName()
        board[Player2_GetY()][Player2_GetX()] = Player2_GetName()

    def GiveUp_Reset():
        global game_over

        var_1 = input(f"Rendirse (s/n): ")

        if var_1.lower() == "s":
            def Game_Over(player: str):
                Jump_Line(1)
                print(f"{Fore.GREEN}#" * 20)
                print(f"{Fore.GREEN}## GANASTE {player.upper()} ##")

                sound_manager.StopAll()
                sound_manager.Play("Win.wav", 0)

            sound_manager.StopAll()
            Game_Over(Player2_GetName())
            sys.exit()

        var_2 = input(f"Reiniciar (s/n): ")

        if var_2.lower() == "s":
            Reset()

    print(f"{Fore.GREEN}## JUEGO ##")
    print(f"{Fore.GREEN}# Ludo divertido #")
    Draw_Players()
    Draw_Board()
    if not on_start:
        GiveUp_Reset()


def Game_Loop(enable_pvp: bool = True):
    def Game_Over(player: str):
        Jump_Line(1)
        print(f"{Fore.GREEN}#" * 20)
        print(f"{Fore.GREEN}## GANASTE {player.upper()} ##")

        sound_manager.StopAll()
        sound_manager.Play("Win.wav", 0)

        input(f"{Fore.GREEN}Presione Enter para terminar ")

    global board, game_over, current_turn, dice, is_pvp, winner
    global p1, p2, px_aux, py_aux

    is_pvp = enable_pvp
    init(autoreset=True)

    Start_1()
    while not game_over:
        Input()
        Update()
        Render()
        current_turn += 1
    Game_Over(winner)

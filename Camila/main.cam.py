# import Gameplay as pvp
import Sound_cam as sound_manager
from colorama import Fore, init


def Select(option: str, limit: int) -> int:
    while not option.isnumeric():
        sound_manager.Play("Error.wav", 1)

        option = input("Ingrese un numero VALIDO: ")

    value = int(option)

    while value < 1 or value > limit:
        sound_manager.Play("Error.wav", 1)

        value = input("Ingrese una opcion VALIDA: ")

        while value.isalpha():
            sound_manager.Play("Error.wav", 1)

            value = input("Ingrese una opcion VALIDA: ")

        value = int(value)

    sound_manager.Play("Enter.wav", 1)
    return value


def Start():
    print()
    print(f'{Fore.GREEN}## MENU DE INICIO ##')
    # print(f'{Fore.MAGENTA}1. Empezar el juego')
    print(f'{Fore.MAGENTA}1. Jugador 1 vs. CPU')
    print(f'{Fore.CYAN}2. Record')
    print(f'{Fore.CYAN}3. Info de jugadores')
    print(f'{Fore.RED}3. Salir')
    print("#" * 20, end="\n")

    option = Select(input("Seleccione una opcion: "), 3)

    print()

    if option == 1:
        Gameplay_1()
    elif option == 2:
        # Record_1()
        ...
    elif option == 3:
        # Info_Player()
        ...
    elif option == 4:
        Quit()


# def Gameplay():
#     print(f'{Fore.GREEN}## TIPO DE JUEGO ##')
#     print(f'{Fore.MAGENTA}1. 1 VS 2')
#     print(f'{Fore.CYAN}2. 1 VS CPU')
#     print(f"{Fore.RED}3. Retroceder")
#     print("#" * 20)
#
#     option = Select(input("Seleccione una opcion: "), 3)
#
#     if option == 1:
#         pvp.Game_Loop()
#     elif option == 2:
#         pvp.Game_Loop(enable_pvp=False)
#     elif option == 3:
#         Start()
info_player={}
def Gameplay_1():
    global info_player
    print(f"{Fore.GREEN }## Registro de jugador ##")

    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    fecha = input("Ingrese su fecha: ")
    nuevo = fecha.split('-')

    info_player["Nombre"] = nombre
    info_player["Correo"] = correo
    info_player["Fecha"] =[int(f) for f in nuevo]

    print("¡Bienvenido,", Fore.YELLOW + nombre, "!")
    print(f"¡Comienza el juego{Fore.CYAN} PV1 vs CPU!")
    print(f"La fecha es: {info_player['Fecha'][0]}-{info_player['Fecha'][1]}")

#
# def Record():
#     file = open("Data/Record.txt", 'r')
#
#     print(f'{Fore.GREEN}## RECORDS ##')
#
#     for cadena in file:
#         print(Fore.CYAN + cadena)
#
#     print("#" * 20)
#     input("Presione Enter para retroceder ")
#
#     sound_manager.Play("Enter.wav", 1)
#
#     Start()
# def Record_1():
#     """
#     1. Create menu "## RECORD ##"
#     2. In "Winner_List_Menu" create menu "## Lista de ganadores ##"
#     3. In "Winner_Month_Menu" create menu "## Ganadores del mes ##"
#     3. And finally include option to go back between menus
#     """
    # def Winner_List_Menu():
    #     print("## Lista de ganadores ##")
    #     print(f"1. El ganador 1 es :{player}")
    #     print(f"2. El ganador 2 es :{player}")
    #     print(f"3. El ganador 3 es :{player}")
    #     print("#" * 20)
    #     input("Presione Enter para retroceder")
    #     sound_manager.Play("Enter.wav", 1)
    #     Record_1()
    #
    # def Winner_Month_Menu():
    #     print(f"Ganadores del mes de")
    #     print(" - Ganador 1")
    #     print(" - Ganador 2")
    #     print(f" Ganadores del mes de")
    #     print(" - Ganador 3")
    #     print("#" * 20)
    #     input("Presione Enter para retroceder")
    #     sound_manager.Play("Enter.wav", 1)
    #     Record_1()
    #
    # print("## RECORD ##")
    # print(f"{Fore.MAGENTA}1. Lista de ganadores")
    # print(f"{Fore.CYAN}2. Ganadores del mes")
    # print(f"{Fore.RED}3. Retroceder")
    # print("#" * 20)
    # option = Select(input("Seleccione una opción: "), 3)
    # print()
    #
    # if option == 1:
    #     Winner_List_Menu()
    # elif option == 2:
    #     Winner_Month_Menu()
    # elif option == 3:
    #     Start()
#
#
# def Info_Player():
#     """
#     1. Create menu "## INFO DE JUGADORES ##"
#     2. In "Search_Player_Menu" create menu "## BUSCAR JUGADOR ##"
#     3. And finally include option to go back between menus
#     """
#     def Search_Player_Menu():
#         ...


def Quit():
    print()


if __name__ == '__main__':
    init(autoreset=True)
    sound_manager.Initialize()
    sound_manager.Play("Theme_main.wav", 0, volume=0.25, loop=True)
    Start()


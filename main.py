import Gameplay as pvp
import Sound as sound_manager
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
        Record_1()
    elif option == 3:
        Info_Player()
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

def Gameplay_1():
    """
    1. Create menu "## Registro de jugador ##"
    2. Request the player's info and save it in dictionary
    3. And finally if the player finished including his info start the game PV1 vs CPU
    """
    ...


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
def Record_1():
    """
    1. Create menu "## RECORD ##"
    2. In "Winner_List_Menu" create menu "## Lista de ganadores ##"
    3. In "Winner_Month_Menu" create menu "## Ganadores del mes ##"
    3. And finally include option to go back between menus
    """

    def Winner_List_Menu():
        ...

    def Winner_Month_Menu():
        ...


def Info_Player():
    """
    1. Create menu "## INFO DE JUGADORES ##"
    2. In "Search_Player_Menu" create menu "## BUSCAR JUGADOR ##"
    3. And finally include option to go back between menus
    """
    def Search_Player_Menu():
        ...


def Quit():
    print()


if __name__ == '__main__':
    init(autoreset=True)
    sound_manager.Initialize()
    sound_manager.Play("Theme_main.wav", 0, volume=0.25, loop=True)
    Start()

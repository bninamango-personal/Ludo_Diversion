import Gameplay as pvp
import Sound as sound_manager
import Info as info_manager
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
    print(f'{Fore.RED}4. Salir')
    print("#" * 20, end="\n")

    option = Select(input("Seleccione una opcion: "), 4)

    print()

    if option == 1:
        pvp.Game_Loop(enable_pvp=False)
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
        print("## LISTA DE GANADORES ##")
        print()

        array = info_manager.Sort_File()

        for i in range(len(array)):
            data = array[i]
            print(f"{data[1]}     {data[0]}     {data[-1]}")

        print()
        print("#" * 20)
        input("Presione Enter para retroceder")
        sound_manager.Play("Enter.wav", 1)
        Record_1()
        print()

    def Winner_Month_Menu():
        print("## GANADORES DEL MES ##")
        month = input("Ingrese su mes: ")
        print()

        array = info_manager.Search_Per_Month(month)

        for i in range(len(array)):
            data = array[i]
            print(f"{data[1]}     {data[0]}     {data[-1]}")

        print()
        print("#" * 20)
        input("Presione Enter para retroceder")
        sound_manager.Play("Enter.wav", 1)
        Record_1()
        print()

    print("## RECORD ##")
    print(f"{Fore.MAGENTA}1. Lista de ganadores")
    print(f"{Fore.CYAN}2. Ganadores del mes")
    print(f"{Fore.CYAN}3. Exportar")
    print(f"{Fore.RED}4. Regresar al menu principal")
    print("#" * 20)
    option = Select(input("Seleccione una opción: "), 3)

    print()

    if option == 1:
        Winner_List_Menu()
    elif option == 2:
        Winner_Month_Menu()
    elif option == 3:
        Start()


def Info_Player():
    """
    1. Create menu "## INFO DE JUGADORES ##"
    2. In "Search_Player_Menu" create menu "## BUSCAR JUGADOR ##"
    3. And finally include option to go back between menus
    """

    def Search_Player_Menu():
        correo = input("Ingrese su correo: ")

        data = info_manager.Get_Player(correo)

        if data != -1:
            nombre = data["Nombre"]
            movimientos = data["Movimientos"]
            copas = data["Copas"]

            print(f"Nombre: {nombre}")
            print(f"Ha ganado {copas} vez")
            print(f"Los movimientos de sus ultimo intento son: \n"
                  f"{movimientos}")

            var_1 = input(f"Exportar (s/n): ")

            if var_1 == 's':
                info_manager.Export_PDF(correo)

        input("Presione Enter para retroceder")
        sound_manager.Play("Enter.wav", 1)
        Info_Player()
        print()

    print(f'{Fore.GREEN}##  INFO DE JUGADORES  ##')
    print(f'{Fore.MAGENTA}1. Buscador jugador')
    print(f"{Fore.RED}2. Regresar al menu principal")
    print("#" * 20)

    option = Select(input("Seleccione una opcion: "), 2)

    if option == 1:
        Search_Player_Menu()
    elif option == 2:
        Start()


def Quit():
    print()


if __name__ == '__main__':
    init(autoreset=True)
    sound_manager.Initialize()
    sound_manager.Play("Theme_main.wav", 0, volume=0.25, loop=True)
    Start()

import Gameplay as pvp
from colorama import Fore, init


def Select(option: str, limit: int) -> int:
    while not option.isnumeric():
        option = input("Ingrese un numero VALIDO: ")

    value = int(option)

    while value < 1 or value > limit:
        value = int(input("Ingrese una opcion VALIDA: "))

    return value


def Start():
    print()
    print(f'{Fore.GREEN}## MENU DE INICIO ##')
    print(f'{Fore.MAGENTA}1. Empezar el juego')
    print(f'{Fore.CYAN}2. Records')
    print(f'{Fore.RED}3. Salir')
    print("#" * 20, end="\n")

    option = Select(input("Seleccione una opcion: "), 3)

    print()

    if option == 1:
        Gameplay()
    elif option == 2:
        Record()
    elif option == 3:
        Quit()


def Gameplay() -> object:
    print(f'{Fore.GREEN}## TIPO DE JUEGO ##')
    print(f'{Fore.MAGENTA}1. 1 VS 2')
    print(f'{Fore.CYAN}2. 1 VS CPU')
    print(f"{Fore.RED}3. Retroceder")
    print("#" * 20)

    option = Select(input("Seleccione una opcion: "), 3)

    if option == 1:
        pvp.Game_Loop()
    elif option == 2:
        pvp.Game_Loop(enable_pvp=False)
    elif option == 3:
        Start()


def Record():
    file = open("../Ludo_Diversion/Data/Record.txt", 'r')

    print(f'{Fore.GREEN}## RECORDS ##')

    for cadena in file:
        print(Fore.CYAN + cadena)

    print("#" * 20)
    input("Presione Enter para retroceder ")

    Start()


def Quit():
    print()


if __name__ == '__main__':
    init(autoreset=True)
    Start()

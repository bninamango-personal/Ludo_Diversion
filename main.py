import Gameplay_PVP as pvp
import Gameplay_PVC as pvc


def Select(option: str) -> int:
    print("#" * 20, end="\n")
    return int(option)


def Start():
    print()
    print('## MENU DE INICIO ##')
    print('1. Empezar el juego')
    print('2. Record')
    print('3. Salir')

    option = Select(input("Seleccione una opcion: "))

    print()

    if option == 1:
        Gameplay()
    elif option == 2:
        Record()
    elif option == 3:
        Quit()


def Gameplay():
    print('## TIPO DE JUEGO ##')
    print('1. 1 VS 2')
    print('2. 1 VS CPU')
    print("3. Retroceder")
    print("#" * 20)

    option = Select(input("Seleccione una opcion: "))

    if option == 1:
        pvp.Game_Loop()
    elif option == 2:
        pvc.Game_Loop()
    elif option == 3:
        Start()


def Record():
    print("Your record ...")

    input("Presione cualquier tecla para retroceder: ")

    Start()


def Quit():
    print()


if __name__ == '__main__':
    Start()

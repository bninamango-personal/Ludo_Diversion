
print('## MENU DE INICIO ##')
def empezar():
    print('1. Empezar el juego')
def record():
    print('2. Record')
def salir():
    print('3. Salir')
empezar()
record()
salir()
print('####################')
opcion1=int(input('Seleccione una opcion: '))

print('')
if opcion1==1:
    print('## TIPO DE JUEGO ##')
    def vs():
        print('1. 1 VS 2')
    def vsCPU():
        print('2. 1 VS CPU')
    vs()
    vsCPU()
    opcion2 = int(input('Seleccione una opcion: '))

    print('')
    if opcion2 == 1:
        print('## Jugadores ##')
        player1 = input('Ingrese el nombre del jugador 1: ')
        player2 = input('ingrese el nombre del jugador 2: ')
        print('####################')
    elif opcion2 == 2:
        print('## Jugadores ##')
        player1 = input('Ingrese el nombre del jugador 1: ')
        print('Jugador 2: CPU')
        print('####################')

    print('')
    print('## JUEGO ##')
    print('# Ludo divertido #')
elif opcion1==2:
    print('Record')
elif opcion1==3:
    print('Gracias por ingresar')

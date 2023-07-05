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
    info_player["Fecha"] = nuevo

    print("¡Bienvenido,", Fore.YELLOW + nombre, "!")
    print(f"¡Comienza el juego{Fore.CYAN} PV1 vs CPU!")
    print(f"La fecha es :{nuevo}")

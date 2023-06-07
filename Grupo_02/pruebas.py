import os #eliminar pantalla
def clearConsole(): #eliminar pantalla
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
clearConsole() #elimninar pantalla
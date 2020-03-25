# pantalla de inicio que maneja la estructura de la app
import Opcion1Menu
import Interface
menu = 1
feed = False

while menu!="0":
    usuario = ""
    user_input = 0

    user_input = input("Bienvenido a DCCahuin!!\nSeleccione una opcion:\n[1]Iniciar Sesion\n[2]Registrar usuario\n[0]Salir\n")

    if user_input == "1":
        usuario = input("Nombre de usuario: ")
        feed = Opcion1Menu.iniciar_sesion(usuario)

    elif user_input == "2":
        Opcion1Menu.registrarse()

    elif user_input == "0":
        menu = user_input


    else:
        print("Input invalido")

    if feed == True:
        print("INICIO DE SESION CORRECTO!!!") #manda al feed principal
        Interface.post()
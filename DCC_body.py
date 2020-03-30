# pantalla de inicio que maneja la estructura de la app
import Opcion1Menu
import Interface
menu = 1
feed = False

while menu!="0" and feed == False:
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
        break


    else:
        print("Input invalido")


while feed == True and menu!=0:
        print("INICIO DE SESION CORRECTO!!!") #manda al feed principal

        user_input = input("[1]Post\n[2]Revisar feed\n[3]Seguir\n[0]Salir\n")

        if user_input == "1":
            Interface.post(usuario)

        elif user_input =="2":
            Interface.feed(usuario)

        elif user_input =="3":
            Interface.follow(usuario)

        elif user_input == "0":
            menu = 0
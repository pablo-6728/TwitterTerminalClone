# pantalla de inicio que maneja la estructura de la app
import FuncionesPrincipales
menu=1

while menu!="0":
    usuario = ""
    user_input = 0

    user_input = input("Bienvenido a DCCahuin!!\nSeleccione una opcion:\n[1]Iniciar Sesion\n[2]Registrar usuario\n[0]Salir\n")

    if user_input == "1":
        usuario = input("Nombre de usuario: ")
        FuncionesPrincipales.iniciar_sesion(usuario)

    elif user_input == "2":
        FuncionesPrincipales.registrarse()

    elif user_input == "0":
        menu = user_input


    else:
        print("Input invalido")


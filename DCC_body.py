# pantalla de inicio que maneja la estructura de la app
import FuncionesPrincipales

def app_DCCahuin():
    usuario = ""
    user_input = 0

    user_input = int(
        input("Bienvenido a DCCahuin!!\nSeleccione una opcion:\n[1]Iniciar Sesion\n[2]Registrar usuario\n[0]Salir\n"))

    if user_input == 1:
        usuario = input("Nombre de usuario: ")

        FuncionesPrincipales.iniciar_sesion(usuario)



app_DCCahuin()

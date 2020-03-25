#pantalla de inicio que maneja la estructura de la app
import FuncionesPrincipales

def app_DCCahuin():

    usuario = ""
    contrasena = ""
    user_input = 0

    user_input= int(input("Bienvenido a DCCahuin!!\nSeleccione una opcion:\n[1]Iniciar Sesion\n[2]Registrar usuario\n[0]Salir"))

    if user_input == 1:
        usuario = input("Nombre de usuario: ")
        contrasena = input("Contrasena: ")

        FuncionesPrincipales.IniciarSesion(usuario, contrasena)

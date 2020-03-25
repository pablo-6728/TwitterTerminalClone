#funcion del programa
user_input = 0

def IniciarSesion(user, password):
    open("usuarios.csv", "r")
    open("post.csv", "r")

    if user in "usuarios.csv" and password in "usuarios.csv:
        return print("Bienvenido a DCCahuin")


    else:
        user_input= input("El usuario no existe\n[1]Intentar otra vez?[2]Registrarse\n[0]Salir")

        if int(user_input) == 1:
            IniciarSesion()
        elif int(user_input) == 2:
            Registrarse()
        elif int(user_input) == 0:
            return 0


def Registrarse():
    pass


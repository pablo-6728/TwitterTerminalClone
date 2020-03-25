# funcion del programa
import csv

user_input = 0


def iniciar_sesion(user):
    User_check = False

    with open("usuarios.csv") as file: #revisar si el usuario existe
        reader = csv.reader(file)

        for column in reader:
            if user == column[0]:
                User_check = True


    if User_check == True:
        print("Inicio de sesion correcto!")
    else:
        print("Login Incorrecto")



def Registrarse():
    pass



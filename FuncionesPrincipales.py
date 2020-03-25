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
        return print("Inicio de sesion correcto!")
    else:
        user_input= input("Login Incorrecto \n[1]Intentar otra vez\n[2]Registrarse\n[0]Salir")
        if user_input == "1":
            print("a.kdsfaksj")
        elif user_input =="2":
            print("2")


def registrarse():
    pass



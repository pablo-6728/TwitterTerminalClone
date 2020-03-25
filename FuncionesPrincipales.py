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

    if User_check == True:      #usuario valido
        return True

    else:       #el usuario no es valido
        user_input= input("Login Incorrecto \n[1]Intentar otra vez\n[2]Registrarse\n")
        if user_input == "1":
            print("\n")

        elif user_input =="2":
            registrarse()



def registrarse():
    new_user = input("\nNombre de usuario: ")
    user_check = False

    with open("usuarios.csv") as file: #revisar si el usuario existe
        reader = csv.reader(file)

        for column in reader:
            if new_user == column[0]:
                user_check = True

    if user_check == True:
        return print("El usuario ya existe")

    else:
        with open("usuarios.csv", "a") as file: #append nuevo usuario
           file.write("\n" + new_user)


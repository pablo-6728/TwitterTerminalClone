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

    alphanumeric = new_user.isalnum() #revisa si el nombre es alfanumerico
    name_lenght = len(new_user)

    if alphanumeric == True and name_lenght >= 8:

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

            with open("seguidores.csv", "a") as file: #append en seguidores
                file.write("\n" + new_user + ",")

    else:
        return print("ERROR: el nombre de usuario tienen que tener 8 caracteres alfanumericos")

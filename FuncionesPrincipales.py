#funcion del programa
import csv
user_input = 0

def IniciarSesion(user, password):
    User_check = False
    Password_check = False

    with open("usuarios.csv") as file: #revisar si el usuario existe
        reader = csv.reader(file)

        for column in reader:
            if user == column[0]:
                User_check = True

    with open("usuarios.csv") as file:
        reader = csv.reader(file)

        for column in reader: #revisa si la contrasena es correcta
            if password == column[1]:
                Password_check = True

    if (User_check == True) and (Password_check == True):
        print("Inicio de sesion correcto!")
    else:
        print("Login Incorrecto")



def Registrarse():
    pass


# feed, post y seguidos
import datetime
import csv
import operator


def post(user):  # permite hacer posts
    new_post = input("Haz tu prograpost (maximo 140 caracteres): \n")

    post_date = datetime.datetime.now()
    real_postdate = str(post_date.year) + "/" + str(post_date.month) + "/" + str(post_date.day)

    if len(new_post) <= 140 and len(new_post) != 0:  # post correcto
        with open("posts.csv", "a") as file:
            file.write("\n" + user + "," + real_postdate + "," + new_post)
            return print("Prograpost enviado")

    elif len(new_post) > 140:  # post con mas caracteres
        return print("Tu post debe tener menos de 140")


    elif len(new_post)==0:  # post vacio
        return print("Tu post no puede estar vacio")


def feed(user):
    post_feed = []


    with open("seguidores.csv", "r") as file:

        reader = csv.reader(file)


        for row in reader:          #los seguidores se guardan en posr feed desde el indice 1
            if row[0] == user:
                post_feed = row

    #tratemos de hacer el sort antes de imprimir
    sort_fechas = open("posts.csv", "r")

    csvr = csv.reader(sort_fechas, delimiter = ",")

    sort = sorted(csvr, key=operator.itemgetter(1))


    for row in sort:
        if row[0] in post_feed:
            print(row)

def follow(user): #funcion para hacer follow

    follow_user = input("Escribe el nombre de usuario de la persona que deseas seguir: ")

    with open("seguidores.csv", "r") as file:
        reader = csv.reader(file)
        followed_users = []

        for row in reader:
            if user in row[0]:
                followed_users = row
                print(followed_users)


                if follow_user in followed_users:    #ya se sigue a este usuario
                    print("Ya sigues a este usuario")


                else:       #este usuario no se sigue
                    with open ("seguidores.csv", "a") as file:
                        if user in row[0]:
                            file.write(follow_user + ",")














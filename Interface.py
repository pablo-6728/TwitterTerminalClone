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


    elif len(new_post) == 0:  # post vacio
        return print("Tu post no puede estar vacio")


def feed(user):
    post_feed = []

    with open("seguidores.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:  # los seguidores se guardan en post feed desde el indice 1
            if row[0] == user:
                post_feed = row

    # tratemos de hacer el sort antes de imprimir
    sort_fechas = open("posts.csv", "r")

    csvr = csv.reader(sort_fechas, delimiter=",")

    sort = sorted(csvr, key=operator.itemgetter(1))

    for row in sort:
        if row[0] in post_feed:
            print(row)


def follow(user):  # funcion para hacer follow

    follow_user = input("Escribe el nombre de usuario de la persona que deseas seguir: ")
    existing_user = False

    with open("usuarios.csv", "rt") as file:  # revisar si el usuario existe
        reader = csv.reader(file)

        for column in reader:
            if follow_user in column:
                existing_user = True


    if existing_user == True:

        if follow_user == user:  # chequeo de uno mismo
            print("No te puedes seguir a ti mismo #sad")

        with open("seguidores.csv", "rt", newline='')as file:
            reader = csv.reader(file)
            followed_users = []
            seguidores = list(reader)  # nuevo csv


        with open("seguidores.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if user in row[0]:
                    followed_users = row


        if follow_user in followed_users:  # ya se sigue a este usuario
            print("Ya sigues a este usuario")


        else:  # este usuario no se sigue
            indice = seguidores.index(followed_users)

            seguidores.remove(followed_users)
            followed_users.append(follow_user)

            seguidores.insert(indice, followed_users)

            with open("seguidores.csv", "w", newline='') as file:           #se anade al csv de usuarios seguidos
               writer = csv.writer(file, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL )
               writer.writerows(seguidores)

        print("Ahora sigues a: " + follow_user)

    elif existing_user == False:
        print("El usuario no existe")


def unfollow(user):
    unfollow_user = input("Escribe el nombre de usuario de la persona que deseas dejar de seguir: ")
    existing_user = False

    with open("usuarios.csv", "rt") as file:  # revisar si el usuario existe
        reader = csv.reader(file)

        for column in reader:
            if unfollow_user in column:
                existing_user = True

    if existing_user == True:

        if unfollow_user == user:  # chequeo de uno mismo
            print("No te puedes dejar de seguir a ti mismo, Todo bien en casa?")

        with open("seguidores.csv", "rt", newline='')as file:
            reader = csv.reader(file)
            followed_users = []
            seguidores = list(reader)  # nuevo csv

        with open("seguidores.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if user in row[0]:
                    followed_users = row

        if unfollow_user in followed_users:  #Aqui esta el usuario que se quiere dejar de seguir

            indice = seguidores.index(followed_users)

            seguidores.remove(followed_users)
            followed_users.remove(unfollow_user)

            seguidores.insert(indice, followed_users)

            with open("seguidores.csv", "w", newline='') as file:  # se anade al csv de usuarios seguidos
                writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerows(seguidores)

            print("Dejaste de seguir a: " + unfollow_user)

        elif unfollow_user not in followed_users:
            print("Tu no sigues a " + unfollow_user)

    elif existing_user == False:
        print("El usuario no existe...")

def borrarPosts(user):
    with open("posts.csv", "rt") as file:
        reader = csv.reader(file)
        own_post = [[],[],[]]   #tus posts guardados
        i = 0

        print("Que post deseas borrar?")

        for row in reader:
            if user in row:
                own_post.append(row)
                i+=1
    i = 0
    while i < len(own_post):
        print(i)
        print(own_post[i])
        print("\n")
        i+=1

    try:
        borrar = int(input("Escribe el numero que esta encima de tu post \n"))
        with open("posts.csv", "rt") as file:       #borrar los posts
            reader = csv.reader(file)
            posts = list(reader)

            print(posts.index(own_post[borrar]))
            posts.remove(own_post[borrar])


        with open("posts.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(posts)

    except:
        print("ERROR!! Intente de nuevo")

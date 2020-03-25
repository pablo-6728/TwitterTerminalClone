#feed, post y seguidos
import datetime
import csv

def post(user): #permite hacer posts
    new_post = input("Haz tu prograpost (maximo 140 caracteres): \n")

    post_date = datetime.datetime.now()
    real_postdate = str(post_date.year) + "/" + str(post_date.month) + "/" + str(post_date.day)

    if len(new_post) <= 140 and len(new_post)!=0:
        with open("posts.csv", "a") as file:
            file.write("\n" + user + "," + real_postdate + "," + new_post)
            return print("Prograpost enviado")

    elif len(new_post) > 140:
        return print("Tu post debe tener menos de 140")


    elif new_post == "":
        return print("Tu post no puede estar vacio")


def feed():
    pass
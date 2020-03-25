#feed, post y seguidos
import datetime
import csv

def post(user): #permite hacer posts
    new_post = input("Haz tu post (maximo 140 caracteres): \n")

    post_date = datetime.datetime.now()
    real_postdate = str(post_date.year) + "/" + str(post_date.month) + "/" + str(post_date.day)

    if len(new_post) <= 140:
        with open("posts.csv", "a") as file:
            file.write(user + "," + real_postdate + "," + new_post)
    else:
        print("Tu post debe tener 140 caracteres o menos")
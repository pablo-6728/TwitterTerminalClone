#feed, post y seguidos
import datetime
import csv
user_input = 0

def post(user):
    new_post = input("Haz tu post (maximo 140 caracteres): \n")

    post_date = datetime.datetime.now()
    real_postdate = str(post_date.year + "/" + post_date.month + "/" + post_date.day)

    if len(new_post) <= 140:
        with open("posts.csv", "a") as file:
            file.write(user + "," + str(post_date) + "," + new_post)

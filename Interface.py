#feed, post y seguidos
import datetime
import csv
user_input = 0

def post():
    new_post = input("Haz tu post (maximo 140 caracteres): \n")
    post_date = datetime.datetime.now()
    if len(new_post) <= 140:
        with open("posts.csv", "a") as file:


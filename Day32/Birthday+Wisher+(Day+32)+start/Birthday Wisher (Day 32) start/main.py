import smtplib
import datetime as dt
import random


def send_email(text: str):
    my_email = 'mlodybartus@gmail.com'
    password = 'tkelpunbstudhbgo'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr='sombodyelse@gmail.com', to_addrs=my_email, msg=f'Subject:Motivation!!!!\n\n {text}')


now = dt.datetime.now()
day = now.day

if now.day == 3:
    # print('Today is the day')
    with open('quotes.txt', 'r') as quotes:
        list_quotes = quotes.readlines()
        quote = random.choice(list_quotes)
        send_email(quote)
        print('Email send!')
import smtplib
import datetime as dt
import random
import os

my_email = os.environ['MY_EMAIL']
password = os.environ['MY_PASS']

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{quote}")







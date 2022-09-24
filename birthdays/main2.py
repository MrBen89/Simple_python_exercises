import smtplib
import datetime as dt
import random

my_email = "b.pearson89@hotmail.com"
my_password = "fishnegg1"

with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

now = dt.datetime.now()

if now.weekday() == 5:
     with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
         connection.starttls()
         connection.login(user= my_email, password= my_password)
         connection.sendmail(
             from_addr=my_email,
             to_addrs="benpearson61@googlemail.com",
             msg=f"Subject:Today's quote\n\nThis is today's quote; \n\n{quote}"
         )

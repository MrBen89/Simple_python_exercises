##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas

my_email = "EMAIL"
my_password = "PASSWORD"

with open("./letter_templates/letter_1.txt") as letter_1_file:
    letter_1 = letter_1_file.read()
with open("./letter_templates/letter_2.txt") as letter_2_file:
    letter_2 = letter_2_file.read()
with open("./letter_templates/letter_3.txt") as letter_3_file:
    letter_3 = letter_3_file.read()

contact_data = pandas.read_csv("./birthdays.csv")
contact_data_frame = pandas.DataFrame(contact_data)
contacts = contact_data_frame.to_dict(orient="records")
print(contacts)

todays_letter_number = random.randint(0, 3)
if todays_letter_number ==0:
    todays_letter = letter_1
elif todays_letter_number ==1:
    todays_letter = letter_2
elif todays_letter_number ==2:
    todays_letter = letter_3

print(type(todays_letter))
now = dt.datetime.now()

for contact in contacts:
    if now.month == contact["month"] and now.day == contact["day"]:
        personal_letter = todays_letter.replace("[NAME]", contact["name"])
        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
             connection.starttls()
             connection.login(user= my_email, password= my_password)
             connection.sendmail(
                 from_addr=my_email,
                 to_addrs="EMAIL",
                 msg=f"Subject:Happy Birthday!\n\n{personal_letter}"
             )

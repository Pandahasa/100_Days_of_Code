##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import random
import smtplib
import pandas

my_email = "sidpanda65@gmail.com"
password = "ztmzwivcwobmtfyf"

from datetime import *

now = datetime.now()
day = now.day
month = now.month
birthdays = pandas.read_csv("birthdays.csv")
information = birthdays.to_dict(orient="records")
for birthday in information:
    if birthday["day"] == day and birthday["month"] == month:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter = file.read()
            name = birthday["name"]
            letter = letter.replace("[NAME]" , name)
            connection = smtplib.SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="sidpanda65@outlook.com", msg=letter)
            connection.close()
            print("yuh")




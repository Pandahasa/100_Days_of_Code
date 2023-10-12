import random
import smtplib

my_email = "sidpanda65@gmail.com"
password = "ztmzwivcwobmtfyf"




from datetime import *

now = datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
    quote = random.choice(all_quotes)
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="sidpanda65@outlook.com", msg=quote)
    connection.close()
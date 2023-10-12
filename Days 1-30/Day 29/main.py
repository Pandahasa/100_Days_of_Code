from tkinter import *
import string
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0 , END)
    all = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for x in range(10):
        password = password + random.choice(all)
    password_entry.insert(0 , password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    writer = f"{website_entry.get()}  |  {email_entry.get()} | {password_entry.get()} \n"
    with open("passwords.txt" , "a") as file:
        file.write(writer)
        file.close()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50 , pady = 50)

canvas = Canvas(width = 200 , height = 200)
lock_png = PhotoImage(file = "logo.png")
canvas.create_image(100 , 100 , image = lock_png)
canvas.grid(column = 1 , row = 0)

text1 = Label(text = "Website")
text1.grid(column = 0 , row = 1)

text2 = Label(text = "Email/Username:")
text2.grid(column = 0 , row = 2)

text3 = Label(text = "Password:")
text3.grid(column = 0 , row = 3)

add_button = Button(text = "Add" , command = save_password , width = 36)
add_button.grid(column = 1 , row = 4 , columnspan = 2 , sticky = EW)

website_entry = Entry(width = 35)
website_entry.grid(column = 1 , row = 1 , columnspan = 2 , sticky = EW)

email_entry = Entry(width = 35)
email_entry.grid(column = 1 , row = 2 , columnspan  = 2 , sticky = EW)

password_entry = Entry(width = 21)
password_entry.grid(column = 1 , row = 3 , sticky = EW)

generate_button = Button(text = "Generate Password" , command = generate_password)
generate_button.grid(column = 2 , row = 3 , sticky = EW)
window.mainloop()
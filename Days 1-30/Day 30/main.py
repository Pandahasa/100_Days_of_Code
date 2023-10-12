import json
from tkinter import *
import string
import random
from tkinter import messagebox

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
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        },
    }
    # writer = f"{website_entry.get()}  |  {email_entry.get()} | {password_entry.get()} \n"
    try:
        with open("data.json" , "r") as file:   
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json" , "w") as file:
            json.dump(new_data, file , indent = 4)
    else:
        data.update(new_data)
        with open("data.json" , "w") as file:
            json.dump(data, file , indent = 4)

            website_entry.delete(0 , END)
            password_entry.delete(0 , END)
            file.close()


def find_password():
    website = website_entry.get()
    try:
        with open("data.json" , "r") as file:
            data = json.load(file)
    except:
        messagebox.showinfo(title = "Error" , message = "File does not exist bro")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website , message = f"Email = {email} \n Password = {password}")
        else:
            messagebox.showinfo(title = "Error" , message = "There's no information for that website")
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
website_entry.grid(column = 1 , row = 1  , sticky = EW)

email_entry = Entry(width = 35)
email_entry.grid(column = 1 , row = 2 , columnspan  = 2 , sticky = EW)

password_entry = Entry(width = 21)
password_entry.grid(column = 1 , row = 3 , sticky = EW)

generate_button = Button(text = "Generate Password" , command = generate_password)
generate_button.grid(column = 2 , row = 3 , sticky = EW)

search_button = Button(text = "Search" , width=13 , command = find_password)
search_button.grid(row=1 , column = 2)
window.mainloop()
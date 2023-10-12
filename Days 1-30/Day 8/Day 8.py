from ntpath import join
from caesarart import logo
from string import ascii_lowercase
from operator import index
encrypt_status = True
print(logo , "\n\nWelcome to Caesar's Code")
shifter = []

def encode(message , shift):
    for letter in message:
        shifter.append(ascii_lowercase.index(letter))
    shifter_new = [ascii_lowercase[(number + shift) % 25] for number in shifter]
    message = "".join(shifter_new)
    print(f"Heres the decoded result: {message}")
    course = input("Type 'no' to stop or 'yes' to continue\n")
    if course == "no":
        encrypt_status = False

def decode(message , shift):
    for letter in message:
        shifter.append(ascii_lowercase.index(letter))
    shifter_new = [ascii_lowercase[(number - shift) % 25] for number in shifter]
    message = "".join(shifter_new)
    print(f"Heres the decoded result: {message}")
    course = input("Type 'no' to stop")
    if course == "no":
        encrypt_status = False
    

while encrypt_status:
    plan = input("Type 'encode' to encrypt or 'decode' to decrypt\n")
    message = input("Type your message\n")
    shift = int(input("Type the shift number\n"))
    shifter = []
    shifter_new = []
    if plan == "encode":
        encode(message , shift)
    else:
        decode(message , shift)



    
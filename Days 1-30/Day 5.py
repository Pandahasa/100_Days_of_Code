import random as rand
from string import ascii_letters, punctuation

password_list = []
print("Welcome to the PyPassword Generator!")
letters = int(input("\nHow many letters would you like in your password? "))
symbols = int(input("\nHow many symbols would you like in your password? "))
numbers = int(input("\nHow many numbers would you like in your password? "))
for x in range(letters):
    randomizer = rand.randint(0,52)
    password_list.append(ascii_letters[randomizer])

for x in range(symbols):
    randomizer = rand.randint(0,31)
    password_list.append(punctuation[randomizer])

for x in range(numbers):
    password_list.append(rand.randint(0,9))

password = ""

for x in range(len(password_list)):
    randomizer = rand.randint(0,len(password_list)-1)
    password += str(password_list[randomizer])
    del(password_list[randomizer])

print(password)
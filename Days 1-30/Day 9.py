from turtle import clear


print("Welcome to the Silent Auction Program")

bidders = {}
bidding = True
highest_bid = 0

def bid(name , price):
    bidders[name] = int(price)

while bidding:
    name = input("What is your name?: ")
    price = input(f"Hello {name} how much would you like to bid? ")
    bid(name , price)
    if int(price) > highest_bid:
        highest_bid = int(price)
        winner = name
    ask = input("Are there any other bidders. Type 'yes' or 'no'")
    if ask == "no":
        bidding = False
    else:
        clear()
        continue

clear()
print("Congratulations the winner is" , winner , "with a bid of" , highest_bid)
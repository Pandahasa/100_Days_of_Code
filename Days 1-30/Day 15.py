MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
coin = 0

def report(resources):
    print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${resources['money']}")

def coin_counter():
    coin = 0.25 * int(input("How many quarters?: "))
    coin += 0.10 * int(input("How many dimes?: "))
    coin += 0.05 * int(input("How many nickels?: "))
    coin += 0.01 * int(input("How many pennies?: "))
    return coin

def enough_money(coin , want , menu , resources, cost):
    if coin < cost['cost']:
            print("Sorry that's not enough money. Money refunded")
            return
    if resources['water'] < menu['water']:
            print("Sorry there is not enough water")
            return
    if resources['milk'] < menu['milk']:
            print("Sorry there is not enough milk")
            return
    if resources['coffee'] < menu['coffee']:
            print("Sorry there is not enough coffee")
            return
    resources['money'] += cost['cost']
    coin -= cost['cost']
    resources['water'] -= menu['water']
    resources['milk'] -= menu['milk']
    resources['coffee'] -= menu['coffee']
    print(f"Here is ${coin} in change")
    print(f"Here is your {want} Enjoy!")

while True:
    want = input("What would you like?  (espresso/latte/cappuccino):  ")
    if want == "report":
        report(resources)
        continue
    coin = coin_counter()
    drink = MENU[want]
    enough_money(coin , want , drink['ingredients'] , resources, MENU[want])
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while True:
    want = input(f"What would you like? {menu.get_items()} :  ")
    if want == "off":
        quit()
    elif want == "report":
        coffee_maker.report()
        money_machine.report()
    drink = menu.find_drink(want)
    if drink:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

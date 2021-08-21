from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo

coffee_maker = CoffeeMaker()
menu = Menu()
coffee_options = menu.get_items()
money_machine = MoneyMachine()

#coffee machine version 2.0
def coffee_machine():
    print(logo)
    coffee_machine_is_running = True
    while coffee_machine_is_running:
        users_request = input(f"What would you like?{coffee_options}")
        if users_request == "report":
            coffee_maker.report()
        elif users_request == "espresso" or users_request == "latte" or users_request == "cappuccino": 
            drink = menu.find_drink(users_request)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            coffee_machine_is_running = False

coffee_machine()
# coffee Machine Program

# import coffee machine logo
# import coffee machine data
from data import *
from logo import *


# function that report the current coffee status
def report_status(water_status, milk_status, coffee_status, money_status):
    print(f"Water: {water_status}")
    print(f"Milk: {milk_status}")
    print(f"Coffee: {coffee_status}")
    print(f"Money: {money_status}")


# function that checks water status
def check_water_status(water_status, users_request):
    if users_request == "espresso":
        if water_status >= 50:
            return True
        else:
            return False
    elif users_request == "latte":
        if water_status >= 200:
            return True
        else:
            return False
    elif users_request == "cappuccino":
        if water_status >= 250:
            return True
        else:
            return False

# function that checks milk status
def check_milk_status(milk_status, users_request):
    if users_request == "espresso":
        return True
    if users_request == "latte":
        if milk_status >= 150:
            return True
        else:
            return False
    elif users_request == "cappuccino":
        if milk_status >= 100:
            return True
        else:
            return False

# function that checks coffee status
def check_coffee_status(coffee_status, users_request):
    if users_request == "espresso":
        if coffee_status >= 18:
            return True
        else:
            return False
    elif users_request == "latte":
        if coffee_status >= 24:
            return True
        else:
            return False
    elif users_request == "cappuccino":
        if coffee_status >= 24:
            return True
        else:
            return False


# function that checks money status
def check_money_status(users_cash, users_request):
    if users_request == "espresso":
        if users_cash >= 1.50:
            return True
        else:
            return False
    elif users_request == "latte":
        if users_cash >= 2.50:
            return True
        else:
            return False
    elif users_request == "cappuccino":
        if users_cash >= 3.00:
            return True
        else:
            return False

# function to run coffee machine
def make_coffee(coffee_resources, coffee_menu):
    # print logo
    print(logo)
    # resources
    water = coffee_resources["water"]
    milk = coffee_resources["milk"]
    coffee = coffee_resources["coffee"]
    money = 0
    #coins 
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01
    # price of coffee
    espresso_price = coffee_menu["espresso"]["cost"]
    latte_price = coffee_menu["latte"]["cost"]
    cappuccino_price = coffee_menu["cappuccino"]["cost"]
    coffee_price = 0

    coffee_machine_turned_on = True

    while coffee_machine_turned_on:
        coffee_prompt = input(
            "What would you like? (espresso/latte/cappuccino)").lower()
        if coffee_prompt == "report":
            report_status(water, milk, coffee, money)
        elif coffee_prompt == "espresso" or coffee_prompt == "latte" or coffee_prompt == "cappuccino":
            if check_water_status(water, coffee_prompt) != True:
                print("Sorry, there's not enough water!")
            elif check_milk_status(milk, coffee_prompt) != True:
                print("Sorry, there's not enough milk!")
            elif check_coffee_status(coffee, coffee_prompt) != True:
                print("Sorry, there's not enough coffee!")
            else:
                print("Insert coin below")
                number_of_quarters = int(input("How many quarters?"))
                number_of_dimes = int(input("How many dimes?"))
                number_of_nickels = int(input("How many nickels?"))
                number_of_pennies = int(input("How many pennies?"))
                total_cash_on_ground = number_of_quarters * quarters + number_of_dimes * \
                    dimes + number_of_nickels * nickels + number_of_pennies * pennies
                if check_money_status(total_cash_on_ground, coffee_prompt):
                    if coffee_prompt == "espresso":
                        coffee_price = espresso_price
                        water -= coffee_menu["espresso"]["ingredients"]["water"]
                        coffee -= coffee_menu["espresso"]["ingredients"]["coffee"]
                    elif coffee_prompt == "latte":
                        coffee_price = latte_price
                        water -= coffee_menu["latte"]["ingredients"]["water"]
                        milk -= coffee_menu["latte"]["ingredients"]["milk"]
                        coffee -= coffee_menu["latte"]["ingredients"]["coffee"]
                    elif coffee_prompt == "cappuccino":
                        coffee_price = cappuccino_price
                        water -= coffee_menu["cappuccino"]["ingredients"]["water"]
                        milk -= coffee_menu["cappuccino"]["ingredients"]["milk"]
                        coffee -= coffee_menu["cappuccino"]["ingredients"]["coffee"]
                    change = round((total_cash_on_ground - coffee_price), 2)
                    money += coffee_price
                    print(f"Here's is your ${change} in change.")
                    print(f"Here's your {coffee_prompt}☕. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money Refunded.")
        elif coffee_prompt == "off":
            coffee_machine_turned_on = False


make_coffee(resources, MENU)



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

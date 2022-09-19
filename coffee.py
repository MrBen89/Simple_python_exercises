# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
#     "money": 0,
# }
# running = True
#
# def take_coins():
#     tens = int(input("How many 10p coins?: "))
#     twenties = int(input("How many 20p coins?: "))
#     fifties = int(input("How many 50p coins?: "))
#     pounds = int(input("How many £1 coins?: "))
#     total_input = (tens *10 + twenties * 20 + fifties *50 + pounds *100)/100
#     return total_input
#
# while running == True:
#
#
#
#     mode = input("What would you like? (esspresso/latte/capuccino): ").lower()
#     if mode == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: £{resources['money']}")
#     if MENU[mode]["ingredients"]["water"] > resources["water"]:
#         print("Sorry, not enough water")
#         running = False
#     elif MENU[mode]["ingredients"]["coffee"] > resources["coffee"]:
#         print("Sorry, not enough coffee")
#         running = False
#     elif "milk" in MENU[mode]["ingredients"] and MENU[mode]["ingredients"]["milk"] > resources["milk"]:
#         print("Sorry, not enough milk")
#         running = False
#     else:
#         print(f"A {mode} costs £{MENU[mode]['cost']}. Please insert coins.")
#         money_taken = take_coins()
#         if money_taken < MENU[mode]["cost"]:
#             print("Sorry, not enough money. Coins refunded")
#         else:
#             resources["water"] -= MENU[mode]["ingredients"]["water"]
#             resources["coffee"] -= MENU[mode]["ingredients"]["coffee"]
#             resources["money"] += MENU[mode]["cost"]
#             if "milk" in MENU[mode]["ingredients"]:
#                 resources["milk"] -= MENU[mode]["ingredients"]["milk"]
#             change = money_taken - MENU[mode]["cost"]
#             print(f"Here's £{change} change. enjoy your {mode}")



#Previous version above. update Object based version below

from coffee_menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from coffee_money import MoneyMachine
running = True

while running:
    menu = Menu()
    coffee = CoffeeMaker()
    money = MoneyMachine()

    order = input(f"What would you like to order? ({menu.get_items()}): ")
    if order == "report":
        coffee.report()
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
            else:
                print("Insufficient funds. Coins returned")
        else:
            print("Insufficient resources.")
            running = False

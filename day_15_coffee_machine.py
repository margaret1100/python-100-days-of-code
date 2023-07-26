from builtins import str
from typing import Dict, Union
import locale

locale.setlocale(locale.LC_ALL, '')

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

profit = 0

resources: Dict[str, int] = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    for resource in resources:
        print(f"{resource.capitalize()} : {resources[resource]}")
    print(f"Money: {locale.currency(profit)}")


def sufficent_resources(coffee_type: str) -> bool:
    ingredients_list = (MENU[coffee_type]['ingredients'])
    for ingredient in ingredients_list:
        if (ingredients_list[ingredient]) > resources[ingredient]:
            return False
    return True


def count_change():
    quarters_amount = int(input('how many quarters?')) * 25
    dimes_amount = int(input('how many dimes?')) * 10
    nickels_amount = int(input('how many nickels')) * 5
    pennies_amount = int(input('how many pennies'))

    total: int = quarters_amount + dimes_amount + nickels_amount + pennies_amount
    return total


def compare_change(coffee_type):
    coffee_cost = MENU[coffee_type]['cost'] * 100
    total_given = count_change()
    if coffee_cost > total_given:
        return 'insufficient'
    else:
        change = (total_given - coffee_cost)/100
        return locale.currency(change)


def remove_resources(coffee_type):
    ingredients_list = (MENU[coffee_type]['ingredients'])
    for ingredient in ingredients_list:
        resources[ingredient] -= ingredients_list[ingredient]
    global profit
    profit += MENU[coffee_type]['cost']


def coffee_machine():
    if sufficent_resources(user_choice):
        print(f"The cost of the {user_choice} is {locale.currency(MENU[user_choice]['cost'])}")
        print("Please insert coins")
        change_comparison: Union[str, str] = compare_change(user_choice)
        if change_comparison == 'insufficient':
            print("Sorry that's not enough money. Money refunded.")
        else:
            if change_comparison == "$0.00":
                print("Thank you, for the exact change!")
            else:
                print(f"Thank you, your change is {change_comparison}")
            print(f"Enjoy your {user_choice}!")
            remove_resources(user_choice)
    else:
        print("insufficient resources to make coffee")
        return


user_choice = ""


while user_choice != "off":
    user_choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if user_choice == "off":
        continue
    elif user_choice == "report":
        print_report()
    elif user_choice in ("espresso", "latte", "cappuccino"):
        coffee_machine()
    else:
        print("Invalid input")


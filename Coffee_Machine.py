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
    "money": 0
}

from art import logo

print(logo)


def print_report():
    """Print the current resources in the coffee machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {resources['money']}$")


def check_resources(user_choice):
    """Check if there are enough resources to make the selected coffee."""
    for ingredient, amount in MENU[user_choice]['ingredients'].items():
        if resources.get(ingredient, 0) < amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True


def insert_coins(user_choice):
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25
    coffee_price = MENU[user_choice]['cost']
    print("Please insert coins.")

    try:
        amount_of_quarters = int(input("how many quarters?: "))
        amount_of_dimes = int(input("how many dimes?: "))
        amount_of_nickels = int(input("how many nickels?: "))
        amount_of_pennies = int(input("how many pennies?: "))
    except ValueError:
        print("Invalid input. Please insert coins again.")
        return False

    sum_of_coins = (quarter * amount_of_quarters) + (dime * amount_of_dimes) + (nickel * amount_of_nickels) + (
                penny * amount_of_pennies)

    if sum_of_coins >= coffee_price:
        change = round(sum_of_coins - coffee_price, 2)
        print(f"Here is ${change} in change.")
        resources['money'] += coffee_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(user_choice):
    """Make the selected coffee and update the resources."""
    for ingredient, amount in MENU[user_choice]['ingredients'].items():
        resources[ingredient] -= amount
    print(f"Here is your {user_choice} ☕️. Enjoy")


machine_on = True

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        print_report()
    elif user_choice == "off":
        machine_on = False
        print("Bye Bye")
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        if check_resources(user_choice):
            transaction_complete = insert_coins(user_choice)
            if transaction_complete:
                make_coffee(user_choice)
    else:
        print("Invalid option, try again.")


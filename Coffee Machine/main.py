# Coffee Machine Program
machine_money = 0


def print_report(resources, money):
    """Prints all the resources in the machine and they money earned."""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')


def check_resources(command, MENU, resources):
    """Checks to see if the machine has enough resources to make the drink"""
    for key, val in MENU[command]["ingredients"].items():
        if resources[key] < val:
            print(f'Sorry there is not enough {key}')
            return False
    return True


def collect_money():
    """Collects the coins from the user and returns the value of the coins received."""
    money = 0.0
    print('Please insert coins.')
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickels = int(input('how many nickels?: '))
    pennies = int(input('how many pennies?: '))
    money += quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return money


def make_coffee(command, MENU, resources):
    """Handle the making of the coffee and return the amt earned from the transaction."""
    can_make_coffee = check_resources(command, MENU, resources)
    if can_make_coffee:
        users_money = collect_money()
        drink_cost = MENU[command]["cost"]
        if users_money >= drink_cost:
            for key, val in MENU[command]["ingredients"].items():
                resources[key] -= val
            users_money -= drink_cost
            if users_money > 0:
                two_dec_user_money = "{:.2f}".format(users_money)
                print(f"Here is ${two_dec_user_money} in change.")
            print(f'Here is your {command} ☕. Enjoy!')
            return drink_cost
        else:
            print("Sorry that's not enough money.  Money refunded.")
    return 0


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
}

while True:
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if command == "off":
        break
    elif command == "report":
        print_report(resources, machine_money)
    elif command in MENU:
        machine_money += make_coffee(command, MENU, resources)
    else:
        print("Invalid choice.  Please try again")

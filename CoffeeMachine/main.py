MENU = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "Macchiato": {
        "ingredients": {
            "milk": 5,
            "coffee": 30,
        },
        "cost": 2.0,
    },
    "Americano": {
            "ingredients": {
                "water": 150,
                "coffee": 18,
            },
            "cost": 2.0,
    },
    "Lungo": {
            "ingredients": {
                "water": 100,
                "coffee": 24,
            },
            "cost": 2.0,
    }
}

profit = 0
resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins(drink_cost):
    """Returns the total calculated from coins inserted."""
    total = 0
    while total < drink_cost:
        print("Please insert coins.")
        quarter = int(input("How many quarters (25 cents)?: "))
        total += quarter * 0.25
        if total >= drink_cost:
            break

        dime = int(input("How many dimes (10 cents)?: "))
        total += dime * 0.1
        if total >= drink_cost:
            break

        nickel = int(input("How many nickels (5 cents)?: "))
        total += nickel * 0.05
        if total >= drink_cost:
            break

        penny = int(input("How many pennies (1 cents)?: "))
        total += penny * 0.01
        if total >= drink_cost:
            break

    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def refill_resources():
    """Refill the resources."""
    resources["water"] = 500
    resources["milk"] = 500
    resources["coffee"] = 500
    print("Resources have been refilled.")


is_on = True

while is_on:
    choice = input("What would you like? (Espresso/Latte/Cappuccino/Macchiato/Americano/Lungo) or (Report/Refill): ")
    if choice == "off":
        is_on = False
    elif choice == "Report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "Refill":
        refill_resources()
    else:
        drink = MENU.get(choice)
        if drink:
            print(f"The price for {choice} is ${drink['cost']}.")
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins(drink["cost"])
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid choice. ⚠️ Please choose from the available options!!!")

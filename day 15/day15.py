# COFFEE MACHINE PROJECT
MENU = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients":{
            "water":250,
            "milk": 100,
            "coffee":24
        },
        "cost": 3.0
    }
}

profit= 0
resources = {
    "milk": 2000,
    "water": 3000,
    "coffee": 800,
}

coins = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins: ")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total
    
def is_transaction_successful(amount_received, drink_cost):
    global profit
    if amount_received >= drink_cost:
        change = round(amount_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enoungh. Money Refunded.")
        return False
    
def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item]-= drink_ingredients[item]
    print(f"Here is your {drink_name}")

admin = 1234

admin_check = input("Are you admin, Type 'Y' or 'N':").lower()

if admin_check == 'y':
    check_admin = int(input("Kindly tell your password: "))
    if check_admin == 1234:
        status_resources = input("Do you want to check the status of the resources, Type 'Y' or 'N': ").lower()
        if status_resources == "y":
            print(resources)
    else:
        print("You have entered the wrong password...")
    
print("1. espresso \n2. latte \n3. cappuccino\n4. Turn Off\n5. report")
correct_order = True
while correct_order:
    order = int(input("What can I make you. 1 | 2 | 3 | 4 | 5: "))

    if order == 1:
        drink = MENU["espresso"]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee("espresso", drink["ingredients"])
    elif order == 2:
        drink = MENU["latte"]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee("latte", drink["ingredients"])
    elif order == 3:
        drink = MENU["cappuccino"]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee("cappuccino", drink["ingredients"])
    elif order == 4:
        print("Turning off the machine....")
        correct_order = False
    elif order == 5:
        print("Here is your machine report:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Profit: ${profit}")
    else:
        print("Kindly choose the correct number....")
        
    anything_else = input("Do you have any other order to make, Type 'Y' or 'N': ").lower()
    if anything_else == "n":
        print(f"Your bill is: ${profit}")
        print("Thank you. Please visit again... 😘😘")
        correct_order = False
    else:
        continue
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

#TODO: 1.Print report of all coffee machine resources
global penny,dime,nickel,quarter,total
OFF = False

while not OFF:
    prompt_input = input("What would you like?(espresso/latte/cappuccino):").lower()
    if prompt_input == "off":
        OFF = True
        print("Device Turning OFF ....")
    elif prompt_input == "report":
        print(f"Resources :-")
        print(f"Water = {resources["water"]}ml")
        print(f"Milk = {resources["milk"]}ml ")
        print(f"Coffee = {resources["coffee"]}g")
    else:
        # TODO: 2. Check whether the resources are sufficient or not to fulfill the order?.
        if MENU[prompt_input]["ingredients"]["water"] > resources["water"] or MENU[prompt_input]["ingredients"]["milk"] > resources["milk"] or MENU[prompt_input]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough resources to get you your order")
        else:
            # TODO: 3. Process Coins: Check if user has inserted enough money to purchase the drink.
            penny = int(input("Enter number of peenies ="))
            dime = int(input("Enter number of dimes ="))
            nickel = int(input("Enter number of nickel ="))
            quarter = int(input("Enter number of quarter ="))
            total = penny * (0.01) + dime * (0.05) + nickel * (0.10) + quarter * (0.25)
            if total >= MENU[prompt_input]["cost"]:
                print(f"Here's your {prompt_input}")
                print(f"Here is ${(round(total - MENU[prompt_input]["cost"])*100)/100} in  change.")
                resources["water"] -= MENU[prompt_input]["ingredients"]["water"]
                resources["milk"] -= MENU[prompt_input]["ingredients"]["milk"]
                resources["coffee"] -= MENU[prompt_input]["ingredients"]["coffee"]
            else:
                print(f"Sorry, the money is insufficient to buy  {prompt_input}")



















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

choice = input(" Choose your coffee latte, cappucino or espresso : \t")
quarter = int(input("how many quarter? \t"))
dime = int(input("how many dime? \t"))
nickel = int(input("how many nickel? \t"))
penny = int(input("how many penny? \t"))

def remaining_money(penny,nickle,dime,quarter,cost=MENU[choice]["cost"]):
    total = penny * 0.01 + nickel * 0.05 + quarter * 0.25 + dime * 0.10
    return total - cost

def resources_update(choice):
    global MENU
    global resources
    if resources["water"]>0  and  resources["coffee"]>0 and resources["milk"]:
        if choice == "espresso":
            resources["water"] -= MENU[choice]["ingredients"]["water"] 
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"] 
        elif choice == "latte":
            resources["water"] -= MENU[choice]["ingredients"]["water"] 
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"] 
        elif choice == "cappuccino"
            resources["water"] -= MENU[choice]["ingredients"]["water"] 
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"] 
    



def coffee_machine(choice,money):
    

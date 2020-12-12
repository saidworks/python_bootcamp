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
try:
    choice = input(" Choose your coffee latte, cappuccino or espresso : \t")
    quarter = float(input("how many quarter? \t"))
    dime = float(input("how many dime? \t"))
    nickel = float(input("how many nickel? \t"))
    penny = float(input("how many penny? \t"))
except ValueError:
    print("Enter a correct data")

def remaining_money(penny,nickel,dime,quarter,cost=MENU[choice]["cost"]):
    total = (penny * 0.01) + (nickel * 0.05) + (quarter * 0.25) + (dime * 0.10)
    return round(total - cost,2)

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
        elif choice == "cappuccino":
            resources["water"] -= MENU[choice]["ingredients"]["water"] 
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"] 
        elif choice == 'report':
            for key,value in resources.items():
                print(f"there is {value} ml left of {key}")
        else:
            for key,value in resources.items():
                print(f"there is {value} ml left of {key}")
    else: 
        print("there is not enough ressources! please contact admin!")
    
    


def coffee_machine(choice):
    resources_update(choice)  
    if remaining_money(penny,nickel,dime,quarter,cost=MENU[choice]["cost"]) >=0:
        print("here is your {} enjoy ☕".format(choice))
        print("here is your remaining money", remaining_money(penny,nickel,dime,quarter,cost=MENU[choice]["cost"]),"$")
    # except KeyError:
    #     print("Your choice is not part of our menu")
    else:
        print("you did not insert enough money! please insert more coin")
if choice in list(MENU.keys()):
    coffee_machine(choice)
else:
    print("Sorry not in our menu!")
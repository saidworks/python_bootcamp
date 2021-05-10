from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# define objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
#work on the choice
order_name = input(f"choose your drink {menu.get_items()} please \t")
if order_name == "report":
    coffee_maker.report()
    money_machine.report()
#process of making coffee
else:
    drink_choice = menu.find_drink(order_name)
    money_machine.make_payment(drink_choice.cost)
    coffee_maker.is_resource_sufficient(drink_choice)
    coffee_maker.make_coffee(drink_choice)









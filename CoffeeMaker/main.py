from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
items = Menu()
# dishes = MenuItem()
machine = MoneyMachine()
machine_status = "ON"
while machine_status == "ON":
    order = input(f"What would you like? ({items.get_items()}) : ")
    if order == "report":
        maker.report()
        machine.report()
        continue
    if order == "latte" or "espresso" or "cappuccino":
        ingredients = items.find_drink(order)
        if maker.is_resource_sufficient(ingredients):
            if machine.make_payment(ingredients.cost):
                maker.make_coffee(ingredients)
    if order == "off":
        machine_status = "OFF"


from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m1 = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

ln = ""
for i in range(30):
        ln+= "-"

OFF = False
while not OFF:
    drink = input(f"What would you like?{m1.get_items()}").lower()
    if drink == "report":
        print(ln)
        cm.report()
        print(ln)
        print(f"Profit = {mm.CURRENCY}{mm.profit}")
        print(ln)
    elif drink == "off":
        OFF =True
        print("Device Turning Off ....")
    else:
        if cm.is_resources_sufficient(m1.find_drink(drink)):
            if mm.make_payment(m1.find_cost(drink)):
                cm.make_coffee(m1.find_drink(drink))










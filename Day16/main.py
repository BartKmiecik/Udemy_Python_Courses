from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    order = input('What coffee would you like? (latte/espresso/capuccino)? :')
    while order == 'report':
        maker.report()
        money_machine.report()
        order = input('What coffee would you like? (latte/espresso/capuccino)? :')

    if maker.is_resource_sufficient(menu.find_drink(order)):
        money_machine.make_payment(menu.find_drink(order).cost)
        maker.make_coffee(menu.find_drink(order))
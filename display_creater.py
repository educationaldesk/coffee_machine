######################################################
# THIS FILE CONTAINS CODE FOR DRINKS & SNACKS DISPLAY.
######################################################

from resources import main_ingredients, snacks, sweeteners
from menu import MENU


def drink_display():
    """this function creates display for drinks"""
    display = {}  # hold all drinks with price.
    closed_drink = 0  # to hold count closed drinks.
    drink_num = 1  # drinks number start from 1.

    for drink in MENU:
        drink_name = drink
        drink_price = MENU[drink]["cost"]
        ingredients_list = MENU[drink]["ingredients"]
        for ingredient in ingredients_list:
            if ingredients_list[ingredient] > main_ingredients[ingredient]:
                closed_drink += 1
                drink_name = "Closed"
                drink_price = "NaN"
                break
        display[str(drink_num)] = [drink_name, drink_price]
        drink_num += 1
    return [closed_drink, display]
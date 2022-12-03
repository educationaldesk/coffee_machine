######################################################
# THIS FILE CONTAINS CODE FOR DRINKS & SNACKS DISPLAY.
######################################################

from resources import main_ingredients, snacks, sweeteners
from menu import MENU


def closed_drinks():
    """this function counts the closed drinks in the menu."""
    closed_drink_count = 0
    for drink in MENU:
        drink_ingredients = MENU[drink]["ingredients"]
        for ingredient in drink_ingredients:
            if main_ingredients[ingredient] < drink_ingredients[ingredient]:
                closed_drink_count += 1
                break
    return closed_drink_count


def drink_display():
    """this function creates display for drinks"""
    display = {}  # hold all drinks with price.
    drink_num = 1  # drinks number start from 1.

    for drink in MENU:
        drink_name = drink
        drink_price = MENU[drink]["cost"]
        ingredients_list = MENU[drink]["ingredients"]
        for ingredient in ingredients_list:
            if ingredients_list[ingredient] > main_ingredients[ingredient]:
                drink_name = "Closed"
                drink_price = "NaN"
                break
        display[str(drink_num)] = [drink_name, drink_price]
        drink_num += 1
    return display


def addon_display(item_list):
    """this function creates the display for addons"""
    display = {}
    serial = 1
    for item in item_list:
        if item_list[item] >= 5:
            display[str(serial)] = item
        serial += 1
    return display

#########################################################
# THIS FILE CONTAINS FUNCTION FOR RESOURCES MANIPULATION
#########################################################
from resources import main_ingredients, snacks, sweeteners, machine_money


def report():
    """this function shows the current state of resources."""
    print("\n============================\nLIST OF MAIN INGREDIENTS\n============================")
    for item in main_ingredients:
        quant = "grm"
        if item == "milk" or item == "cream" or item == "water":
            quant = "ml"
        print(f"{item} : {main_ingredients[item]}{quant}")

    print("\n============================\nLIST OF SNACKS\n============================")
    for snack in snacks:
        print(f"{snack} we have {snacks[snack]}")

    print("\n============================\nLIST OF SWEETENERS\n============================")
    for sweet in sweeteners:
        print(f"{sweet} we have {sweeteners[sweet]}")

    print("\n============================\nTOTAL MONEY WE HAVE IS:")
    print(f"₹{machine_money[0]}")
    print("============================\n")
    if input("like to added resources  press x to cancel: ") == 'y':
        return add_resources("y")


def add_resources(var='x'):
    """this function is added resources"""
    if var == 'x':
        report()
    else:
        for ingredient in main_ingredients:
            print(f"{ingredient} : {main_ingredients[ingredient]}")
            main_ingredients[ingredient] += int(input(f"enter {ingredient} or 0 then enter >>> "))

        for snack in snacks:
            print(f"{snack} : {snacks[snack]}")
            snacks[snack] += int(input(f"enter {snack} or 0 then enter >>> "))

        for sweet in sweeteners:
            print(f"{sweet} : {sweeteners[sweet]}")
            sweeteners[sweet] += int(input(f"enter {sweet} or 0 then enter >>> "))

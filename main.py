####################################
# THIS FILE RUNS THE COFFEE MACHINE
####################################

from display_creater import drink_display
from menu import MENU

closed_drinks = drink_display()[0]  # total number of closed drinks.
total_drinks = len(MENU) # total drinks in the menu

if total_drinks == closed_drinks:
    print("SORRY.\nMACHINE OUT OF ORDER.😭")
else:
    run_machine = True

    while run_machine:
        # drink variables.
        drinks_list = drink_display()[1]  # drinks_display imported from display creator.
        available_drinks = {num: drinks_list[num] for num in drinks_list if drinks_list[num][0] in MENU}

        if input("close machine : ") != 'r':
            run_machine = False

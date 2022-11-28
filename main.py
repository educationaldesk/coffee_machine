####################################
# THIS FILE RUNS THE COFFEE MACHINE
####################################

from display_creater import closed_drinks, drink_display
from resources import main_ingredients
from menu import MENU


not_available_drinks = closed_drinks()  # tracks closed drinks due to lack of resources
total_drinks = len(MENU)  # total drinks in MENU, both open and closed

if total_drinks <= not_available_drinks:
    print("SORRY\nMACHINE IS OUT OF ORDER😭.")
else:
    run_machine = True  # variable to run the coffee machine

    while run_machine:
        display = drink_display()  # display is a dictionary hold drink names and cost and serial number.
        avail_drinks = {num: [display[num][0], display[num][1]] for num in display if display[num][0] in MENU}
        avail_drinks_list = [num for num in avail_drinks]

        # menu and display code starts here.
        print("WELCOME\nSELECT A DRINK.\nMENU. we have >>\n")
        for i in display:
            print(f"{i}. {display[i][0]} @ rs. {display[i][1]}")

        if input("enter x to close : ") == 'x':
            run_machine = False

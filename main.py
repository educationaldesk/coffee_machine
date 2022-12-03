####################################
# THIS FILE RUNS THE COFFEE MACHINE
####################################

from display_creater import closed_drinks, drink_display, addon_display
from resources import main_ingredients, snacks, snack_price, sweeteners, sweet_price
from command import user_commands
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
        drinks_serial_no = [num for num in avail_drinks]  # creates the drinks number.
        total_order_price = 0  # gathers the total price of drinks.

        # menu and display code starts here.
        print("WELCOME\nSELECT A DRINK.\nMENU. we have >>\n")
        for i in display:
            print(f"{i}. {display[i][0]} @ ₹{display[i][1]}")

        order = user_commands(drinks_serial_no)  # takes order from customer and employees
        if order == 'x':
            run_machine = False
        elif order == "report":
            pass
        elif order in avail_drinks:
            print(f"you ordered {order}. {avail_drinks[order][0]} @ ₹{avail_drinks[order][1]}\n")
            total_order_price += avail_drinks[order][1]  # adding price in total.

            # sweetener variables.
            sweetener_display = addon_display(sweeteners)
            sweetener_list = [num for num in sweetener_display]
            for item in sweetener_display:
                print(f"{item}. {sweetener_display[item][0]} @ ₹{sweetener_display[item][1]}")
            sweetener_order = user_commands(sweetener_list)  # taking sweetener order.

            if sweetener_order in sweetener_display:
                print(f"You ordered {sweetener_order} @ ₹{sweetener_display[sweetener_order][1]}")
                total_order_price += sweetener_display[sweetener_order][1]

            # snacks variables starts here.
            snack_display = addon_display(snacks)
            snack_list = [num for num in snack_display]
            for item in snack_display:
                print(f"{item}. {snack_display[item][0]} @ ₹{snack_display[item][1]}")
            snack_order = user_commands(snack_list)  # taking snacks order.

            if snack_order in snack_display:
                print(f"You ordered {snack_order} @ ₹{snack_display[snack_order][1]}")
                total_order_price += snack_display[snack_order][1]

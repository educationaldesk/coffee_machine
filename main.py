####################################
# THIS FILE RUNS THE COFFEE MACHINE
####################################

from display_creater import closed_drinks, drink_display, addon_display
from resources import main_ingredients, snacks, snack_price, sweeteners, sweet_price
from money import money_checker
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

        # customer order details.
        customer_order = {}
        total_order_price = 0

        # menu and display code starts here.
        print("WELCOME\nSELECT A DRINK.\nMENU. we have >>\n")
        for i in display:
            print(f"{i}. {display[i][0]} @ ₹{display[i][1]}")

        order = user_commands(drinks_serial_no)  # takes order from customer and employees
        if order == 'x':  # this turns off the machine
            run_machine = False
        elif order == "report":  # shows all the resources
            pass
        elif order in avail_drinks:  # for drink that is available
            print(f"you ordered {order}. {avail_drinks[order][0]} @ ₹{avail_drinks[order][1]}\n")
            customer_order[avail_drinks[order][0]] = avail_drinks[order][1]
            total_order_price += avail_drinks[order][1]  # adding price in total.

            # sweetener variables.
            sweetener_display = addon_display(sweeteners)  # created sweetener dictionary
            sweetener_list = [num for num in sweetener_display]
            for item in sweetener_display:  # list all the sweeteners
                print(f"{item}. {sweetener_display[item]} @ ₹{sweet_price}")
            sweetener_order = user_commands(sweetener_list)  # taking sweetener order.

            if sweetener_order in sweetener_display:  # checking sweetener in list.
                print(f"You ordered {sweetener_order} @ ₹{sweet_price}\n")
                customer_order[sweetener_display[sweetener_order]] = sweet_price
                total_order_price += sweet_price

            # snacks variables starts here.
            snack_display = addon_display(snacks)  # snacks dictionary
            snack_list = [num for num in snack_display]
            for item in snack_display:
                print(f"{item}. {snack_display[item]} @ ₹{snack_price}")
            snack_order = user_commands(snack_list)  # taking snacks order.

            if snack_order in snack_display:
                print(f"You ordered {snack_order} @ ₹{snack_price}\n")
                customer_order[snack_display[snack_order]] = snack_price
                total_order_price += snack_price

            print("\n")
            for item in customer_order:
                print(f"{item} for ₹{customer_order[item]}")
            print("==========================")
            print(f"Total price: ₹{total_order_price}")

            money_entered = money_checker(total_order_price)  # hold customer input
            print(f"==================================")
            if money_entered:
                print(f"PAID: ₹{money_entered} - REQUIRED: ₹{total_order_price} = REFUND: ₹{money_entered - total_order_price}")
            else:
                print(f"PAID: ₹{money_entered}")
                print("Insufficient Money.\nORDER CANCELLED.\n\n")

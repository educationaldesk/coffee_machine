######################################################################
# contains code for all the command for drinks, snacks and sweeteners
######################################################################

def user_commands(drinks_list):
    """this function takes commands for drinks."""
    user_input = input(f"please select from {drinks_list} : ")
    if user_input in drinks_list or user_input == "report" or user_input == 'x':
        return user_input
    else:
        return user_commands(drinks_list)

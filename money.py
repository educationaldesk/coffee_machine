#####################################
# THIS FILE CONTAINS MONEY FUNCTION
#####################################

def money_checker(total_money):
    """this function checker if total money entered"""
    currency = {
        "1": 1,
        "5": 5,
        "10": 10,
        "20": 20
    }
    collection = 0

    for worth in currency:
        user_input = input(f"enter ₹{worth}s or press other button to cancel > ")
        if not user_input.isnumeric():
            collection = False
            break
        collection += (round(float(user_input), 2)) * currency[worth]
    if collection < total_money:
        collection = False
    return collection

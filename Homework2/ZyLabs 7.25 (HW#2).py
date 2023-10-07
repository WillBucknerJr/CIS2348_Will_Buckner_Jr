# Will Buckner Jr#
# PS_ID: 2101260#
def exact_change(user_total):
    num_dollars = user_total // 100
    user_total = user_total % 100
    num_quarters = user_total // 25
    user_total = (user_total % 25)
    num_dimes = user_total // 10
    user_total = (user_total % 10)
    num_nickels = user_total // 5
    user_total = (user_total % 5)
    num_pennies = user_total

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    change_input = int(input())
    dollars, quarters, dimes, nickels, pennies = exact_change(change_input)

    if dollars == 1:
        print("1 dollar")
    elif dollars > 1:
        print(f"{dollars} dollars")

    if quarters == 1:
        print("1 quarter")
    elif quarters > 1:
        print(f"{quarters} quarters")

    if dimes == 1:
        print("1 dime")
    elif dimes > 1:
        print(f"{dimes} dimes")

    if nickels == 1:
        print("1 nickel")
    elif nickels > 1:
        print(f"{nickels} nickels")

    if pennies == 1:
        print("1 penny")
    elif pennies > 1:
        print(f"{pennies} pennies")

    if dollars == 0:
        if quarters == 0:
            if dimes == 0:
                if nickels == 0:
                    if pennies == 0:
                        print("no change")

# Will Buckner Jr#
# PS_ID: 2101260#
def find_variables():
    x_coefficient1 = int(input(""))
    y_coefficient1 = int(input(""))
    total1 = int(input(""))
    x_coefficient2 = int(input(""))
    y_coefficient2 = int(input(""))
    total2 = int(input(""))
    for x in range(-10, 11):
        for y in range(-10, 11):
            if ((x * x_coefficient1) + (y * y_coefficient1)) == total1:
                if ((x * x_coefficient2) + (y * y_coefficient2)) == total2:
                    return print(f"{x} {y}")
    else:
        return print("No solution")


find_variables()

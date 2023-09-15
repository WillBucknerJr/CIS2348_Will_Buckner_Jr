#Will Buckner Jr#
#PSID: 2101260#

import math
height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
area = (height * width)
paint_needed = (area / 350)
print("Wall area:", area, "square feet")
print("Paint needed:", '{:.2f}'.format(paint_needed), "gallons")
print("Cans needed:", math.ceil(paint_needed), "can(s)\n")

color = (input("Choose a color to paint the wall:\n"))
color_price = {"red": 35, "blue": 25, "green": 23}
print(f"Cost of purchasing {color} paint: ${color_price[color] * math.ceil(paint_needed)}")

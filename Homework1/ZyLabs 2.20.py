#Will Buckner Jr#
#PSID: 2101260#

lemon_juice = float(input("Enter amount of lemon juice (in cups):"))
water = float(input("Enter amount of water (in cups):"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):"))
serving_size = float(input("How many servings does this make?"))
print('Lemonade ingredients - yields', '{:.2f}'.format(serving_size), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar')

user_serving_size = float(input("How many servings would you like to make?"))
user_lemon_juice = (lemon_juice * (user_serving_size / serving_size))
user_water = (water * (user_serving_size / serving_size))
user_agave_nectar = (agave_nectar * (user_serving_size / serving_size))
print('Lemonade ingredients - yields', '{:.2f}'.format(user_serving_size), 'servings')
print('{:.2f}'.format(user_lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(user_water), 'cup(s) water')
print('{:.2f}'.format(user_agave_nectar), 'cup(s) agave nectar')

print('Lemonade ingredients - yields', '{:.2f}'.format(user_serving_size), 'servings')
print('{:.2f}'.format(user_lemon_juice / 16), 'gallon(s) lemon juice')
print('{:.2f}'.format(user_water / 16), 'gallon(s) water')
print('{:.2f}'.format(user_agave_nectar / 16), 'gallon(s) agave nectar')

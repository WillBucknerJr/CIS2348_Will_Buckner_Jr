#Will Buckner Jr#
#PSID: 2101260#

from datetime import date
current_month = int(input("Enter current month:"))
current_day = int(input("Enter current day:"))
current_year = int(input("Enter current year:"))
user_birthday_month = int(input("Enter your birthday month:"))
user_birthday_day = int(input("Enter your birthday day:"))
user_birthday_year = int(input("Enter your birthday year:"))
avar = (date(current_year, current_month, current_day))
bvar = (date(user_birthday_year, user_birthday_month, user_birthday_day))
num_of_days = (avar - bvar).days

if (current_month == user_birthday_month) and (current_day == user_birthday_day):
    print("Birthday Calculator")
    print("Current day")
    print(f"Month: {current_month}")
    print(f"Day: {current_day}")
    print(f"Year: {current_year}")
    print("Birthday")
    print("Month:", user_birthday_month)
    print("Day:", user_birthday_day)
    print("Year:", user_birthday_year)
    print(f"You are {int(num_of_days / 365)} years old.")
    print("Happy Birthday!")
else:
    print("Birthday Calculator")
    print("Current day")
    print(f"Month: {current_month}")
    print(f"Day: {current_day}")
    print(f"Year: {current_year}")
    print("Birthday")
    print("Month:", user_birthday_month)
    print("Day:", user_birthday_day)
    print("Year:", user_birthday_year)
    print(f"You are {int(num_of_days / 365)} years old.")

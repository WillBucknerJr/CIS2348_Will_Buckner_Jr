# Will Buckner Jr#
# PS_ID: 2101260#
from datetime import datetime


def is_valid_date(date_string):
    date1 = datetime.strptime(date_string, '%B %d, %Y')
    if date1 <= datetime.now():
        return date1 <= datetime.now()
    else:
        return False


while True:
    date_str = input("Enter a date (e.g., March 1, 1990), or -1 to quit: ")

    if date_str == '-1':
        break
    # Extract Date
    date_start = date_str.find(" ")
    date_end = date_str.find(',', date_start)
    if date_start != -1 and date_end != -1:
        date = date_str[date_start + 1:date_end]

        if is_valid_date(date_str):
            formatted_date = datetime.strptime(date_str, '%B %d, %Y').strftime('%m/%d/%Y')
            print(formatted_date)
        else:
            continue
    else:
        continue

# Will Buckner Jr#
# PS_ID: 2101260#
from datetime import datetime


def is_valid_date(date_string):
    date1 = datetime.strptime(date_string, '%B %d, %Y')
    if date1 <= datetime.now():
        return date1 <= datetime.now()
    else:
        return False


file_name = input()
my_file = open(file_name, "r")
output_file = open("parsedDates.tx", "w")
zero = 0
reading = my_file.readlines()

with my_file, output_file:
    for x in reading:
        if "\n" in x:
            replacement = x.replace("\n", "")
            reading[zero] = replacement
            zero += 1
        else:
            zero += 1

    for xy in reading:
        date_str = xy
        if date_str == '-1':
            break
        # Extract Date #
        date_start = date_str.find(" ")
        date_end = date_str.find(',', date_start)
        if date_start != -1 and date_end != -1:
            date = date_str[date_start + 1:date_end]

            if is_valid_date(date_str):
                formatted_date = datetime.strptime(date_str, '%B %d, %Y').strftime('%m/%d/%Y')
                print(formatted_date)
                output_file.write(f'{formatted_date}\n')
            else:
                continue
        else:
            continue

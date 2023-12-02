# Will Buckner Jr#
# PSID: 2101260#

parts = input().split()
name = parts[0]
while name != '-1':
    try:
        if parts[1] == str:
            raise ValueError

        else:
            age = int(parts[1]) + 1
            print(f'{name} {age}')
    except ValueError as error:
        print(f"{name} {0}")

    parts = input().split()
    name = parts[0]

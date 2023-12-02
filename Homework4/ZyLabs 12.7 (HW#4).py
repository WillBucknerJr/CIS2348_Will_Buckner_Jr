# Will Buckner Jr#
# PSID: 2101260#

def get_age():
    age = int(input())
    if 17 >= age or age > 75:
        raise ValueError("Invalid age.")
    return age


def fat_burning_heart_rate(age):
    heart_rate1 = (.7 * (220 - age))
    return heart_rate1


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate} bpm")
    except ValueError as error:
        print(error)
        print(f"Could not calculate heart rate info.\n")

# Will Buckner Jr#
# PS_ID: 2101260#
weak_password = input("")
new = ""


def strong_password(a):
    new_password = a.replace("i", "!")
    new_password = new_password.replace("a", "@")
    new_password = new_password.replace("m", "M")
    new_password = new_password.replace("B", "8")
    new_password = new_password.replace("o", ".")
    return print(f"{new_password + 'q*s'}")


strong_password(weak_password)

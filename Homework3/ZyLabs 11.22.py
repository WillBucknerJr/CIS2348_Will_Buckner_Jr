# Will Buckner Jr#
# PSID: 2101260#
sentence = input()
xlist = sentence.split(" ")
storage = {}

for x in xlist:
    if x not in storage:
        storage[x] = 1
    else:
        storage[x] += 1


for y in xlist:
    print(f"{y} {storage[y]}")

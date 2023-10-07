# Will Buckner Jr#
# PS_ID: 2101260#
import csv

file_name = input()
myfile = open(file_name, "r")
file = csv.reader(myfile, delimiter=";")
jab = {}

for line in file:
    texter = line[0]
    new_list = texter.split(",")
    for x in new_list:
        if x not in jab:
            jab[x] = 1
        else:
            jab[x] += 1

for x in jab:
    print(x, jab[x])

myfile.close()

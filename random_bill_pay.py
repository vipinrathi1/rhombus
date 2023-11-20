import random

name_string = input("Give me everybody's names, separated by a comma. \n")
names = name_string.split(",")
n = len(names)
n = n-1
x = random.randint(0, n)
print(f"Bill will be paid by {names[x]}")

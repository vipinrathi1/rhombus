print("Welcome to the love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1_lower = name1.lower()
name2_lower = name2.lower()
name = name1_lower + name2_lower
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")
# e = name.count("e")
true = t + r + u + e
love = l + o + v + e
score = str(true) + str(love)
score = int(score)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score >= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

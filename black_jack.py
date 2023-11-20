import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []

def deal_user():
    card = random.choice(cards)
    user.append(card)

def deal_computer():
    card = random.choice(cards)
    computer.append(card)

deal_user()
deal_user()
deal_computer()
deal_computer()

user_total = sum(user)
if user_total == 22:
    user = [11, 1]
    user_total = sum(user)

print(f"Your cards are {user}")

print(f"Your total is {user_total}")
computer_total = sum(computer)
if computer_total == 22:
    computer = [11, 1]
    computer_total = sum(computer)
print(f"Computer's first card is {computer[0]}")

if computer_total == 21:
    print("'BLACKJACK' Computer Won")


elif user_total == 21:
    print("'BLACKJACK' You won")

else:
    user_choice = input("Do you want another card? type 'yes' or 'no':").lower()
    if user_choice == "no":
        while computer_total < 17:
            deal_computer()
            computer_total = sum(computer)
            if computer_total > 21:
                i = 11
                if i in user:
                    a = user.index(11)
                    user[a] = 1
                    computer_total = sum(computer)

                else:
                    print(f"You have won the game. computer cards are {computer} and total is {computer_total}")
                    break

            print(f"Computer cards are {computer}")
            print(f"Computer total is {computer_total}")

    while user_choice == "yes":
        deal_user()
        user_total = sum(user)
        if user_total > 21:
            i = 11
            if i in user:
                a = user.index(11)
                user[a] = 1
                user_total = sum(user)
            else:
                print(f"You have lost the game. Your cards are {user} and total is {user_total}")
                break

        print(f"Your cards are {user}")
        print(f"Your total is {user_total}")
        user_choice = input("Do you want another card? type 'yes' or 'no':").lower()
    if user_total > computer_total and user_total < 22:
        print(f"You have won the game. computer total is {computer_total} and computer cards are {computer}")
    elif user_total < computer_total and computer_total < 22:
        print(f"You have lost the game. computer total is {computer_total} and computer cards are {computer}")
    elif user_total == computer_total:
        print(f"It's a draw. User:{user_total}, Computer:{computer_total}")






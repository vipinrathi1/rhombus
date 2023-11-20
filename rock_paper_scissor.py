import random
choices = ["Rock", "Paper", "Scissor"]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissor \n"))
com_choice = random.randint(0,2)
if player_choice > 2:
    print("You have chosen invalid option. You Loose")
else:
    print(f"You have chosen {choices[player_choice]}")
    print(f"Computer has chosen {choices[com_choice]}")

if player_choice == com_choice:
    print("It's a Draw")
elif player_choice == 0:
    if com_choice == 1:
        print("Computer Won!")
    else:
        print("You Won")
elif player_choice == 1:
    if com_choice == 0:
        print("You Won")
    else:
        print("Computer Won!")
elif player_choice == 2:
    if com_choice == 0:
        print("Computer Won!")
    else:
        print("You Won")

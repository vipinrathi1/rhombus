print("Welcome to the Treasure Game! \nYou need to find the treasure")
choice1 = input("choose a direction! Left or Right? \n")
choice1 = choice1.capitalize()
if choice1 == "Right":
    print("Your game is over")
elif choice1 == "Left":
    # print("You have chosen the right path")
    choice2 = input("choose between Swim or Wait? \n")
    choice2 = choice2.capitalize()
    if choice2 == "Swim":
        print("Your game is over")
    elif choice2 == "Wait":
        choice3 = input("choose among the 3 doors! Red, Blue or Yellow? \n")
        choice3 = choice3.capitalize()
        if choice3 == "Yellow":
            print("Congratulations!!! You have WON the game!!!")
        elif choice3 == "Red" or "Yellow":
            print("You have lost the game")

 
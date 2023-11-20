import random
import hangman_words
import hangman_art
images = hangman_art.stages
print(hangman_art.logo)
word_list = hangman_words.word_list
word = random.choice(word_list)
# print(chosen_word)
chosen_word = list(word)
guessed_word = []
display = []
for i in range(len(chosen_word)):
    display.append("_")
print(display)

lives = 6
while not display == chosen_word and lives > 0:
    print(images[lives])
    guess = input("\nGuess a letter: ").lower()


    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess in guessed_word:
        print("You have already guessed this letter! \n")
    elif guess in chosen_word:
        print("Correct guess ")
    elif guess not in chosen_word:
        lives -= 1
        print(f"You have guessed a wrong letter. You have {lives} lives left \n")

    guessed_word.append(guess)

    print(display)

    if display == chosen_word:
        print("CONGRATULATIONS!!! You have WON the game")
    elif lives == 0:
        print(images[lives])
        print("GAME OVER! 'YOU LOSE'")
        print(f"Word is {word}")




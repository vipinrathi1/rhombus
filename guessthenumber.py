import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input((f'Guess your number form 1 to {x}: ')))
        if guess > random_number:
            print(' pick a lower number.')
        elif guess < random_number:
            print('pick a higher number. ')
    print('Your have guessed the right number.')
guess(10)

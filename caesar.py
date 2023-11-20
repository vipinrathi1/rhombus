
import math
import caesar_art
print(caesar_art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue is True:

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(text, shift):

        word = ""
        for i in text:
            if i in alphabet:
                n = alphabet.index(i)

                if direction == "encode":
                    n += shift
                    if n > 25:
                        x = math.floor(n / 26)
                        n = n - 26 * x
                elif direction == "decode":
                    n -= shift
                    if n < 0:
                        x = math.floor(n / 26)
                        n = n + 26 * abs(x)
                word += alphabet[n]

            else:
                word += i
        print(f"This is the result '{word}'")


    caesar(text, shift)
    result = input("Type 'Yes' to play again and 'No' to stop: ").capitalize()
    if result == "No":
        should_continue = False
        print("Goodbye")











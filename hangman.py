
import random

words = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]

print("==============================")
print("        COLORS OF LIFE")
print("==============================")
print("Guess the hidden color!")
print("You have 6 chances.")

word = random.choice(words)
display = ["_"] * len(word)

wrong_guesses = 0

while wrong_guesses < 6 and "_" in display:

    print("\nColor:", " ".join(display))
    print("Wrong guesses:", wrong_guesses)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter!")
        continue

    if guess in word:
        print("Correct! Nice guess!")

        for count in range(len(word)):
            if word[count] == guess:
                display[count] = guess

    else:
        wrong_guesses = wrong_guesses + 1
        print("Oops! Try another letter.")

if "_" not in display:
    print("\nCongratulations! You guessed the color!")
    print("You won!")
else:
    print("\nGame over! Better luck next time.")

print("The color was:", word)
print("Thanks for playing Colors of Life!")

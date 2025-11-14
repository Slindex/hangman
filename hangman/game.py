from . import config as cf
from .helpers import (
    wordGenerator,
    difficultySelector,
    masking,
    attemptsUpdate,
    maskUpdate,
    printColored
)


def run_game():
    word = wordGenerator()
    mask_percent = difficultySelector()
    mask = masking(word, mask_percent)

    print()
    print(" ".join(mask))
    print()
    print(f"Remaining attempts: {cf.MAX_ATTEMPTS}")

    while cf.MAX_ATTEMPTS > 0:
        guess = input("Guess a letter or a word: ")
        print()

        if len(guess) == len(word):
            if guess == word:
                printColored("You win!", "green")
                return
            else:
                printColored("Wrong word", "red")
                attemptsUpdate()
                continue

        if len(guess) != 1:
            printColored("Enter only ONE letter", "yellow")
            print()
            print("Remaining attempts:", cf.MAX_ATTEMPTS)
            continue

        if guess in word:
            maskUpdate(word, mask, guess)
            print(" ".join(mask))
            printColored(f"Right Char!: {guess}", "green")
        else:
            printColored(f"Wrong char: {guess}", "red")
        
        if "".join(mask) == word:
            printColored("You win!", "green")
            return
        
        attemptsUpdate()

    printColored(f"You lost! The word was {word}", "red")
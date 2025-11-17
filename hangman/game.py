from . import config as cf
from .helpers import (
    themeSelector,
    wordGenerator,
    difficultySelector,
    masking,
    attemptsUpdate,
    maskUpdate,
    printColored,
    askNewGame
)


def run_game():
    theme = themeSelector()
    mask_percent = difficultySelector()

    gameLoop(theme, mask_percent)

    while askNewGame() == "y":
        gameLoop(theme, mask_percent)
    
    print()
    print("Thanks for playing!")


def gameLoop(theme: str, mask_percent: float):
    word = wordGenerator(theme)
    mask = masking(word, mask_percent)
    remaining_attempts = cf.MAX_ATTEMPTS

    print()
    print(" ".join(mask))

    while remaining_attempts > 0:
        print()
        print("Remaining attempts:", remaining_attempts)
        guess = input("Guess a letter or a word: ")
        print()

        if len(guess) == len(word):
            if guess == word:
                printColored("You win!", "green")
                print()
                return
            else:
                printColored("Wrong word", "red")
                remaining_attempts -= 1
                continue

        if len(guess) != 1:
            printColored("Enter only ONE letter", "yellow")
            continue

        if guess in word:
            maskUpdate(word, mask, guess)
            print(" ".join(mask))
            printColored(f"Right Char!: {guess}", "green")
        else:
            printColored(f"Wrong char: {guess}", "red")
        
        if "".join(mask) == word:
            printColored("You win!", "green")
            print()
            return
        
        remaining_attempts -= 1
    
    printColored(f"You lost! The word was {word}", "red")
    print()

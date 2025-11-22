import random as rd
from . import config as cf
from .loader import load_words
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
    words = load_words(theme)

    gameLoop(theme, mask_percent, words)

    while askNewGame() == "y":
        gameLoop(theme, mask_percent, words)
    
    print()
    print("Thanks for playing!")


def gameLoop(theme: str, mask_percent: float, words: list[str]):
    word = rd.choice(words)
    mask = masking(word, mask_percent)
    remaining_attempts = cf.MAX_ATTEMPTS

    if "".join(mask) == word:
        words.remove(word)
        printColored("You win!", "green")
        print()
        return

    print()
    print(" ".join(mask))

    while remaining_attempts > 0:
        print()
        print("Remaining attempts:", remaining_attempts)
        guess = input("Guess a letter or a word: ")
        print()

        if len(guess) == len(word):
            if guess == word:
                words.remove(word)
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
            continue
        else:
            printColored(f"Wrong char: {guess}", "red")
        
        remaining_attempts -= 1
    
    printColored(f"You lost! The word was {word}", "red")
    print()

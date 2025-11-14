from . import config as cf
from .helpers import wordGenerator, masking, maskUpdate, attemptsUpdate


def run_game():
    word = wordGenerator()
    mask = masking(word)

    print(" ".join(mask))
    print(f"Remaining attempts: {cf.MAX_ATTEMPTS}")

    while cf.MAX_ATTEMPTS > 0:
        guess = input("Guess a letter or a word: ")

        if len(guess) == len(word):
            if guess == word:
                print("You win!")
                return
            else:
                print("Wrong word")
                attemptsUpdate()
                continue

        if len(guess) != 1:
            print("Enter only ONE letter")
            continue

        if guess in word:
            maskUpdate(word, mask, guess)
            print(" ".join(mask))
        else:
            print("Wrong char")
        
        if "".join(mask) == word:
            print("You win!")
            return
        
        attemptsUpdate()
    
    print(f"You lost! The word was {word}")
from . import config as cf
from .helpers import wordGenerator, masking, maskUpdate


def run_game():
    word = wordGenerator()
    mask = masking(word)
    attempts = 0

    print(" ".join(mask))

    while attempts < cf.MAX_ATTEMPTS:
        guess = input("Guess a letter or a word: ")

        if len(guess) == len(word):
            if guess == word:
                print("You win!")
                return
            else:
                print("Wrong word")
                attempts += 1
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
        
        attempts += 1
    
    print(f"You lost! The word was {word}")
import random as rd
import config as cf


def wordGenerator():
    return rd.choice(cf.WORDS)

def masking(word: str) -> list:
    mask = [*word]
    num_chars = int(len(mask) * cf.HIDDEN_RATIO)
    hidden_chars = rd.sample(range(len(mask)), num_chars)

    for i in hidden_chars:
        mask[i] = "_"  

    return mask

def maskUpdate(word: str, mask: list, guess: str):
    for i in range(len(word)):
        if word[i] == guess:
            mask[i] = guess
    
    print(" ".join(mask))
    

def main():
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
        else:
            print("Wrong char")
        
        if "".join(mask) == word:
            print("You win!")
            return
        
        attempts += 1
    
    print(f"You lost! The word was {word}")


if __name__ == "__main__":
    main()
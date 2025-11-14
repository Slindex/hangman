import random as rd
import config as cf


def wordGenerator():
    return rd.choice(cf.WORDS)

def masking(word: str) -> list[str]:
    mask = [*word]
    num_chars = int(len(mask) * cf.HIDDEN_RATIO)
    hidden_chars = rd.sample(range(len(mask)), num_chars)

    for i in hidden_chars:
        mask[i] = "_"  

    return mask

def maskUpdate(word: str, mask: list[str], guess: str):
    for i in range(len(word)):
        if word[i] == guess:
            mask[i] = guess
    
    print(" ".join(mask))
import random as rd
from .loader import load_words
from . import config as cf


def wordGenerator() -> str:
    words = load_words()

    if len(words) == 0:
        raise ValueError("No hay palabras disponibles para jugar")

    return rd.choice(words)

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

def attemptsUpdate():
    cf.MAX_ATTEMPTS -= 1
    print(f"Remaining Attempts: {cf.MAX_ATTEMPTS}")

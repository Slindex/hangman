import random as rd
from .loader import load_words
from . import config as cf
from colorama import Fore, Style


def wordGenerator() -> str:
    theme = themeSelector()
    words = load_words(theme)

    if len(words) == 0:
        raise ValueError("No hay palabras disponibles para jugar")

    return rd.choice(words)

def masking(word: str, percent: float) -> list[str]:
    mask = [*word]
    num_chars = int(len(mask) * percent)
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
    print()
    print(f"Remaining Attempts: {cf.MAX_ATTEMPTS}")

def themeSelector() -> str:
    print("\nChoose a theme:\n")
    for key, value in cf.THEMES.items():
        print(f"{key}: {value[:-4]}")
    print()

    choice = input("Option:").strip()

    if choice not in cf.THEMES:
        raise ValueError(f"Choose a valid option: {list(cf.THEMES.keys())}")

    theme = cf.THEMES[choice]
    
    return theme

def difficultySelector() -> float:
    print("\nChoose a difficulty\n")
    for key, value in cf.DIFFICULTY.items():
        print(f"{key}: {value['name']}")
    print()

    choice = input("Option:").strip()

    if choice not in cf.DIFFICULTY:
        raise ValueError(f"Choose a valid option: {list(cf.DIFFICULTY.keys())}")
    
    mask_percent = cf.DIFFICULTY[choice]['percent']

    return mask_percent

def printColored(text: str, color: str):
    colors = {
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "red": Fore.RED,
    }

    if color not in colors:
        raise ValueError(f"Invalid color {color}")

    print(f"{colors[color] + text + Style.RESET_ALL}")

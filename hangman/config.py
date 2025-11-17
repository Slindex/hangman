from colorama import Fore
import os

# Game
MAX_ATTEMPTS = 5
THEMES = {
    "1": "champions.txt",
    "2": "items.txt",
    "3": "teams.txt",
    "4": "api-pokemon",
    "5": "countries.txt",
    "6": "capitals.txt",
}
DIFFICULTY = {
    "1": {"name": "Easy", "percent": 0.3},
    "2": {"name": "Medium", "percent": 0.5},
    "3": {"name": "Hard", "percent": 0.7},
}
COLORS = {
    "green": Fore.GREEN,
    "yellow": Fore.LIGHTYELLOW_EX,
    "red": Fore.RED,
}

# Cache
CACHE_EXPIRE_HOURS = 24

# Paths
BASE_DIR = os.path.dirname(__file__)
CACHE_PATH = os.path.join(BASE_DIR, "data", "cache")

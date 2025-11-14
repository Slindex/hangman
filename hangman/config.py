from colorama import Fore


MAX_ATTEMPTS = 5
THEMES = {
    "1": "champions.txt",
    "2": "items.txt",
    "3": "teams.txt",
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

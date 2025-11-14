import os


BASE_DIR = os.path.dirname(__file__)
WORDS_PATH = os.path.join(BASE_DIR, "data", "words.txt")

def load_words():
    try:
        with open(WORDS_PATH, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"No se encuentra el archivo words.txt en {os.path.dirname(WORDS_PATH)}")
        return []
    
    return words

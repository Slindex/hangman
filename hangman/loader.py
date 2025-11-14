import os


BASE_DIR = os.path.dirname(__file__)

def load_words(theme: str):
    FILE_PATH = os.path.join(BASE_DIR, "data", theme)

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"No se encuentra el archivo words.txt en {os.path.dirname(FILE_PATH)}")
        return []
    
    return words

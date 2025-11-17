import os
import requests
import json
from datetime import datetime
from .cache import caching
from . import config as cf


def load_words(theme: str):
    if theme == "api-pokemon":
        return load_pokemon_api()
    
    FILE_PATH = os.path.join(cf.BASE_DIR, "data", theme)

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"No se encuentra el archivo words.txt en {os.path.dirname(FILE_PATH)}")
        return []
    
    return words

def load_pokemon_api(limit=200) -> list[str]:
    FILE_NAME = "pokemon.json"
    FILE_PATH = os.path.join(cf.CACHE_PATH, FILE_NAME)

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        dct = json.load(f)
    
    last_update = datetime.fromisoformat(dct['last_update'])
    current_date = datetime.now()
    hours = (current_date - last_update).total_seconds() / 3600

    if hours <= cf.CACHE_EXPIRE_HOURS:
        print("Retrieved from cache")
        return dct['data']

    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()['results']
    names = [item['name'] for item in data]

    print("Caching API data")
    caching(names, FILE_NAME)
    
    return names

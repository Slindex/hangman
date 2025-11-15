import json
import os
from . import config as cf
from datetime import datetime


def caching(data: list[str], file_name: str):
    FILE_PATH = os.path.join(cf.CACHE_PATH, file_name)

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        dct = json.load(f)
    
    timestamp = datetime.now().isoformat(timespec="seconds")

    dct['data'] = data
    dct['last_update'] = timestamp

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(dct, f, indent=4)         

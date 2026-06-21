def saluer(nom):
    return f"Bonjour, {nom} !"

def additionner(a, b):
    return a + b

if __name__ == "__main__":
    print(saluer("DevOps"))

def multiplier(a, b):
    return a * b

import datetime

def log(message):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {message}")

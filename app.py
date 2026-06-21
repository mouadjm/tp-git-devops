def saluer(nom):
    return f"Bonjour, {nom} !"

def additionner(a, b):
    return a + b

if __name__ == "__main__":
    print(saluer("DevOps"))

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

from app import saluer, additionner

def test_saluer():
    assert saluer("Alice") == "Bonjour, Alice !"

def test_additionner():
    assert additionner(2, 3) == 5

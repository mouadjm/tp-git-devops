from app import saluer, additionner

def test_saluer():
    assert saluer("Alice") == "Bonjour, Alice !"

def test_additionner():
    assert additionner(2, 3) == 5

def test_diviser():
    assert diviser(10, 2) == 5.0

def test_diviser_par_zero():
    import pytest
    with pytest.raises(ValueError):
        diviser(10, 0)

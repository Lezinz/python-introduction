from src.romanNumeral import romanNumeral

def test_romanNumeral():
    assert romanNumeral(1) == "I"
def test_romanNumeral2():
    assert romanNumeral(2) == "II"
def test_romanNumeral3():
    assert romanNumeral(3) == "III"
def test_romanNumeral4():
    assert romanNumeral(4) == "IV"
def test_romanNumeral3999():
    assert romanNumeral(3999) == "MMMCMXCIX"
def test_romanNumeral4000():
    assert romanNumeral(4000) == "Le chiffre est trop grand"

from src.romanNumeral import romantoint

def test_roman_to_int_I():
    assert romantoint("I") == 1
def test_roman_to_int_II():
    assert romantoint("II") == 2
def test_roman_to_int_III():
    assert romantoint("III") == 3
def test_roman_to_int_IV():
    assert romantoint("IV") == 4
def test_roman_to_int_MMMCMXCIX():
    assert romantoint("MMMCMXCIX") == 3999
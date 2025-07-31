from src.romanNumeral import romanNumeral, romantoint

def test_romanNumeral_de_base():
    assert romanNumeral(1) == "I"
    assert romanNumeral(2) == "II"
    assert romanNumeral(3) == "III"
    assert romanNumeral(4) == "IV"
    assert romanNumeral(5) == "V"
    assert romanNumeral(6) == "VI"
    assert romanNumeral(9) == "IX"
    assert romanNumeral(10) == "X"
    assert romanNumeral(40) == "XL"
    assert romanNumeral(49) == "XLIX"
    assert romanNumeral(90) == "XC"
    assert romanNumeral(400) == "CD"
    assert romanNumeral(900) == "CM"
    assert romanNumeral(1987) == "MCMLXXXVII"
    assert romanNumeral(3999) == "MMMCMXCIX"
    assert romanNumeral(4000) == "Le chiffre est trop grand"

def test_romantoint_de_base():
    assert romantoint("I") == 1
    assert romantoint("II") == 2
    assert romantoint("III") == 3
    assert romantoint("IV") == 4
    assert romantoint("V") == 5
    assert romantoint("VI") == 6
    assert romantoint("IX") == 9
    assert romantoint("X") == 10
    assert romantoint("XL") == 40
    assert romantoint("XLIX") == 49
    assert romantoint("XC") == 90
    assert romantoint("CD") == 400
    assert romantoint("CM") == 900
    assert romantoint("MCMLXXXVII") == 1987
    assert romantoint("MMMCMXCIX") == 3999
from src.romanNumeral import entier_vers_chiffre_romain, chiffre_romain_vers_entier

def test_conversion_entier_en_chiffre_romain():
    assert entier_vers_chiffre_romain(1) == "I"
    assert entier_vers_chiffre_romain(4) == "IV"
    assert entier_vers_chiffre_romain(9) == "IX"
    assert entier_vers_chiffre_romain(58) == "LVIII"
    assert entier_vers_chiffre_romain(1994) == "MCMXCIV"

def test_conversion_chiffre_romain_en_entier():
    assert chiffre_romain_vers_entier("I") == 1
    assert chiffre_romain_vers_entier("IV") == 4
    assert chiffre_romain_vers_entier("IX") == 9
    assert chiffre_romain_vers_entier("LVIII") == 58
    assert chiffre_romain_vers_entier("MCMXCIV") == 1994
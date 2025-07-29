#Ouverture fonction #romanNumeral

def romanNumeral(number: int) -> str:
    if number > 3999:
        return "Le chiffre est trop grand"
    result = ""

    #Tableau de valeur (valeur, symbole)

    Entier_Romain = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    #Calcul pour trouver le symbole

    for valeur, symbole in Entier_Romain:
        while number >= valeur:
            result += symbole
            number -= valeur

    return result

def romantoint(symbole: str) -> int:
    result = ""


def jn(number: int) -> str:
    if number <= 0:
        return "Le nombre doit être supérieur à 0"
    valeurs = [
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
        (1, 'I'),
    ]

    resultat = ""
    for (valeur, symbole) in valeurs:
        count = number // valeur
        resultat += symbole * count
        number -= valeur * count

    return resultat



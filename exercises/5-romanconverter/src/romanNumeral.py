# write code here
def jn():
    return ""

def entier_vers_chiffre_romain(nombre_entier):
    tableau_conversion = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    resultat = ""
    for valeur, chiffre in tableau_conversion:
        while nombre_entier >= valeur:
            resultat += chiffre
            nombre_entier -= valeur
    return resultat

def chiffre_romain_vers_entier(texte_romain):
    dictionnaire_conversion = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    valeur_precedente = 0

    for caractere in reversed(texte_romain):
        valeur = dictionnaire_conversion[caractere]
        if valeur < valeur_precedente:
            total -= valeur
        else:
            total += valeur
            valeur_precedente = valeur
    return total

# === Démonstration simple ===
if __name__ == "__main__":
    # Exemple : convertir un entier en romain
    entier = 1994
    romain = entier_vers_chiffre_romain(entier)
    print(f"{entier} devient en romain : {romain}")

    # Exemple : convertir un romain en entier
    texte = "MMXXV"
    entier_resultat = chiffre_romain_vers_entier(texte)
    print(f"{texte} devient en entier : {entier_resultat}")
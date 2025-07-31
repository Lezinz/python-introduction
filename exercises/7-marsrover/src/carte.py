class Carte:
    def __init__(self):
        self.grille = [
            ["🟩","🟩","🌳","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🌳","🟩"],
            ["🟩","🌳","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩"],
        ]

    def afficher(self):
        for ligne in self.grille:
            print("".join(ligne))

    def afficher_avec_rover(self, rover):
        copie = []
        for ligne in self.grille:
            copie.append(ligne[:])

        copie[rover.y][rover.x] = rover.symbole()

        for ligne in copie:
            print("".join(ligne))
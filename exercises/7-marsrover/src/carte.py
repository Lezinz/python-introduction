class Carte:
    def __init__(self):
        self.grille = [
            ["🟩", "🟩", "🌳", "🟩", "🟩"],
            ["🟩", "🟩", "🟩", "🟩", "🟩"],
            ["🟩", "🟩", "🟩", "🌳", "🟩"],
            ["🟩", "🌳", "🟩", "🟩", "🟩"],
            ["🟩", "🟩", "🟩", "🟩", "🟩"]
        ]

    def afficher_carte(self):
        for ligne in self.grille:
            print("".join(ligne))

    def afficher_avec_rover(self, rover):
        copie = [ligne[:] for ligne in self.grille]
        copie[rover.y][rover.x] = rover.symbole()
        for ligne in copie:
            print("".join(ligne))

    def afficher_apres_deplacement(self, rover):
        self.afficher_avec_rover(rover)
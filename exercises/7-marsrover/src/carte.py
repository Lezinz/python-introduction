class Carte:
    def __init__(self):
        self.grille = [
            ["🟩", "🟩", "🌳", "🟩", "🟩"],
            ["🟩", "🟩", "🟩", "🟩", "🟩"],
            ["🟩", "🟩", "🟩", "🌳", "🟩"],
            ["🟩", "🌳", "🟩", "🟩", "🟩"],
            ["➡️", "🟩", "🟩", "🟩", "🟩"]
        ]

    def afficher(self):
        for ligne in self.grille:
            print("".join(ligne))
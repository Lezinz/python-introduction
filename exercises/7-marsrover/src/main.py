from carte import Carte
from rover import Rover

carte = Carte()
rover = Rover(0, 4, "E")

commandes = ["⬆️", "➡️", "⬆️", "⬆️", "⬅️", "⬆️"]

for commande in commandes:
    if commande == "➡️":
        rover.tourner_droite()
    elif commande == "⬅️":
        rover.tourner_gauche()
    elif commande == "⬆️":
        rover.avancer(carte)

carte.afficher_avec_rover(rover)
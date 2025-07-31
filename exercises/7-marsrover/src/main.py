from carte import Carte
from rover import Rover

carte = Carte()
rover = Rover(0, 4, "E")

print("Étape 1 : Carte seule")
carte.afficher_carte()

print("Étape 2 : Carte avec rover")
carte.afficher_avec_rover(rover)
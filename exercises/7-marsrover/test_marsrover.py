from src.rover import Rover

def test_init_rover():
    r = Rover(2, 4, "N")
    assert (r.x, r.y) == (2, 4)
    assert r.direction == "N"

def test_advance_rover():
    class Carte:
        grille = [["🟩"]*5 for _ in range(5)]
    r = Rover(2, 4, "N")
    r.avancer(Carte())
    assert (r.x, r.y) == (2, 3)

def test_turn_left():
    r = Rover(2, 4, "N")
    r.tourner_gauche()
    assert r.direction == "W"
    r.tourner_gauche()
    assert r.direction == "S"

def test_turn_right():
    r = Rover(2, 4, "N")
    r.tourner_droite()
    assert r.direction == "E"
    r.tourner_droite()
    assert r.direction == "S"

def test_advance_blocked_by_obstacle():
    grille = [
        ["🟩","🟩","🌳","🟩","🟩"],
        ["🟩","🟩","🟩","🟩","🟩"],
        ["🟩","🟩","🟩","🌳","🟩"],
        ["🟩","🌳","🟩","🟩","🟩"],
        ["🟩","🟩","🟩","🟩","🟩"],
    ]

    class Carte:
        def __init__(self):
            self.grille = grille

    carte = Carte()

    r = Rover(2, 3, "E")
    r.avancer(carte)
    assert (r.x, r.y) == (3, 3)

    r = Rover(2, 2, "E")
    r.avancer(carte)
    assert (r.x, r.y) == (2, 2)
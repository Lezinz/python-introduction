from src import *

def test_joueur_nul():
    bowling = Bowling("-- -- -- -- -- -- -- -- -- --")
    assert bowling.calculate() == 0

def test_toutes_les_boules_1():
    bowling = Bowling("11 11 11 11 11 11 11 11 11 11")
    assert bowling.calculate() == 20

def test_score_aléatoire():
    bowling = Bowling("9- 81 72 63 54 45 36 27 18 09")
    assert bowling.calculate() == 90

def test_cinq_et_zero():
    bowling = Bowling("50 50 50 50 50 50 50 50 50 50")
    assert bowling.calculate() == 50

def test_quatre_et_un():
    bowling = Bowling("46 46 46 46 46 46 46 46 46 46")
    assert bowling.calculate() == 100

def test_tous_les_spares():
    bowling = Bowling("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5")
    assert bowling.calculate() == 150

def test_tous_les_strikes():
    bowling = Bowling("X X X X X X X X X X X X")
    assert bowling.calculate() == 300




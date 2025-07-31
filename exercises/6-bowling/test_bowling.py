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

def test_strike_suivi_de_9_et_0():
    bowling = Bowling("X 90 -- -- -- -- -- -- -- --")
    assert bowling.calculate() == 28  # 10 + 9 + 0 = 19 + 9

def test_spare_suivi_de_9_et_0():
    bowling = Bowling("5/ 90 -- -- -- -- -- -- -- --")
    assert bowling.calculate() == 10 + 9 + 9

def test_spare_en_dernier_avec_bonus():
    bowling = Bowling("-- -- -- -- -- -- -- -- -- 5/5")
    assert bowling.calculate() == 10 + 5

def test_strike_en_dernier_avec_bonus():
    bowling = Bowling("-- -- -- -- -- -- -- -- -- X 11")
    assert bowling.calculate() == 10 + 1 + 1

def test_mixte_strike_spare_normal():
    bowling = Bowling("X 5/ 72 9- X 3/ 61 X X 44")
    assert bowling.calculate() == 148
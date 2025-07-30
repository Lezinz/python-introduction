from src import *

def test_shitty_player():
    bowling = Bowling("-- -- -- -- -- -- -- -- -- --")
    assert bowling.calculate() == 0

def test_full1():
    bowling = Bowling("11 11 11 11 11 11 11 11 11 11")
    assert bowling.calculate() == 20

def test_aléatoire():
    bowling = Bowling("9- 81 72 63 54 45 36 27 18 09")
    assert bowling.calculate() == 90

def test_cinq_et_zero():
    bowling = Bowling("50 50 50 50 50 50 50 50 50 50")
    assert bowling.calculate() == 50

def test_quatre_et_1():
    bowling = Bowling("46 46 46 46 46 46 46 46 46 46")
    assert bowling.calculate() == 100
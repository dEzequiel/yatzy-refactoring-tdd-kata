import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance([1, 2, 3, 4, 5])
    assert 14 == Yatzy.chance([1, 1, 3, 3, 6])
    assert 21 == Yatzy.chance([4, 5, 5, 6, 1])


def test_yatzy():
    assert 50 == Yatzy.yatzy([1, 1, 1, 1, 1])
    assert 0 == Yatzy.yatzy([1, 2, 1, 1, 1])
    assert 0 == Yatzy.yatzy([1, 3, 1, 1, 1])
    assert 50 == Yatzy.yatzy([2, 2, 2, 2, 2])

def test_ones():
    assert 0 == Yatzy.ones([3, 3, 3, 4, 5])
    assert 5 == Yatzy.ones([1, 1, 1, 1, 1])    

# @pytest.fixture
# def inyector():
#     # Es el setup de unittest o de JUnit
#     tirada = Yatzy(1, 2, 3, 4, 5)
#     return tirada


# def test_fours(inyector):
#     # Es necesario un objeto ya creado
#     valorEsperado = 4
#     # No puedo testear con fixtures = inyeccion de dependencias
#     # los metodos estaticos como chance()
#     assert valorEsperado == inyector.fours()
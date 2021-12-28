import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_constructor():
    x = Yatzy([1, 2, 3, 4, 5])
    assert x == Yatzy([-1, 2, 3, 4, 5])


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
    assert 2 == Yatzy.ones([1, 3, 3, 1, 5])
    assert 5 == Yatzy.ones([1, 1, 1, 1, 1])
    assert 0 == Yatzy.ones([2, 3, 4, 5, 6])
    assert 0 == Yatzy.ones([3, 3, 3, 4, 5])


def test_twos():
    assert 0 == Yatzy.twos([3, 3, 3, 4, 5])
    assert 10 == Yatzy.twos([2, 2, 2, 2, 2])
    assert 4 == Yatzy.twos([1, 3, 2, 4, 2])


def test_threes():
    assert 9 == Yatzy.threes([3, 3, 3, 4, 5])
    assert 15 == Yatzy.threes([3, 3, 3, 3, 3])
    assert 0 == Yatzy.threes([1, 2, 4, 5, 6])
    assert 0 == Yatzy.threes([1, 1, 1, 1, 1])


def test_fours():
    assert 20 == Yatzy.fours([4, 4, 4, 4, 4])
    assert 4 == Yatzy.fours([1, 2, 3, 4])
    assert 0 == Yatzy.fours([1, 2, 3, 5])


def test_fives():
    assert 25 == Yatzy.fives([5, 5, 5, 5, 5])
    assert 5 == Yatzy.fives([1, 2, 3, 4, 5])
    assert 0 == Yatzy.fives([1, 2, 3, 4, 6])


def test_sixes():
    assert 30 == Yatzy.sixes([6, 6, 6, 6, 6])
    assert 6 == Yatzy.sixes([1, 2, 3, 4, 6])
    assert 0 == Yatzy.sixes([1, 2, 3, 4, 5])


def test_score_pair():
    assert 10 == Yatzy.score_pair([2, 2, 2, 5, 5])
    assert 12 == Yatzy.score_pair([5, 5, 6, 6, 1])
    assert 0 == Yatzy.score_pair([1, 2, 3, 4, 5])


def test_two_pair():
    assert 8 == Yatzy.two_pair([1, 1, 1, 3, 3])
    assert 4 == Yatzy.two_pair([2, 2, 1, 3, 4])
    assert 6 == Yatzy.two_pair([1, 1, 2, 2, 3])
    assert 10 == Yatzy.two_pair([2, 2, 2, 3, 3])


def test_four__of_akind():
    assert 8 == Yatzy.four_of_a_kind([2, 2, 2, 2, 5])
    assert 0 == Yatzy.four_of_a_kind([1, 2, 3, 4, 5])


def test_three_of_a_kind():
    assert 12 == Yatzy.three_of_a_kind([3, 4, 4, 4, 5])
    assert 0 == Yatzy.three_of_a_kind([5, 5, 5, 5, 4])
    assert 9 == Yatzy.three_of_a_kind([6, 5, 3, 3, 3])
    assert 15 == Yatzy.three_of_a_kind([5, 1, 2, 5, 5])
    assert 3 == Yatzy.three_of_a_kind([1, 1, 1, 4, 3])


def test_small_straight():
    assert 0 == Yatzy.small_straight([1, 2, 3, 3, 5])
    assert 15 == Yatzy.small_straight([1, 2, 3, 4, 5])
    assert 0 == Yatzy.small_straight([2, 3, 4, 5, 6])
    assert 0 == Yatzy.small_straight([1, 3, 4, 5, 5])
    assert 0 == Yatzy.small_straight([6, 6, 6, 6, 6])
    assert 0 == Yatzy.small_straight([1, 2, 3, 4, 6])


def test_large_straight():
    assert 20 == Yatzy.large_straight([2, 3, 4, 5, 6])
    assert 0 == Yatzy.large_straight([1, 2, 3, 4, 5])
    assert 0 == Yatzy.large_straight([1, 3, 4, 5, 5])
    assert 0 == Yatzy.large_straight([6, 6, 6, 6, 6])
    assert 0 == Yatzy.large_straight([1, 2, 3, 4, 6])


def test_full_house():
    assert 8 == Yatzy.full_house([1, 1, 2, 2, 2])
    assert 0 == Yatzy.full_house([1, 3, 1, 3, 2])
    assert 12 == Yatzy.full_house([3, 3, 2, 2, 2])
    assert 8 == Yatzy.full_house([1, 1, 2, 2, 2])
    assert 14 == Yatzy.full_house([4, 2, 2, 4, 2])


# @pytest.fixture
# def inyector():
#     # Es el setup de unittest o de JUnit
#     tirada = Yatzy(1, 2, 3, 4, 5)
#     return tirada


# def test_fours(inyector):
#     # Es necesario un object ya creado
#     valorEsperado = 4
#     # No puedo testear con fixtures = inyeccion de dependencias
#     # los metodos estaticos como chance()
#     assert valorEsperado == inyector.fours()

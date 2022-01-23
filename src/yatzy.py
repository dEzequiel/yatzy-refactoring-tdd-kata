from random import Random
import random
from src import pips
from src.pips import Pips
from functools import reduce

class Yatzy:
    
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(dice):
        return sum(dice)

    @staticmethod
    def yatzy(dice):

        comparing_number = random.choice(dice)
        for value in dice:
            if comparing_number != value:
                return 0
        return 50

    @staticmethod
    def ones(dice):
        ONE = Pips.ONE.value
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(dice):
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(dice):
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE

    @staticmethod
    def fours(dice):
        FOUR = Pips.FOUR.value
        return dice.count(FOUR) * FOUR

    @staticmethod
    def fives(dice):
        FIVE = Pips.FIVE.value
        return dice.count(FIVE) * FIVE

    @staticmethod
    def sixes(dice):
        SIX = Pips.SIX.value
        return dice.count(SIX) * SIX

    @staticmethod
    def score_pair(dice):
        PAIR = 2
        for pip in Pips.reversed_values():
            if dice.count(pip) >= 2:
                return pip * PAIR
        return 0

    @staticmethod
    def two_pair(dice):
        PAIR = 2
        pairs = set([value for value in dice if dice.count(value) >= PAIR])
        if len(pairs) == PAIR:
            return sum([value * 2 for value in pairs])
        return 0

    @staticmethod
    def three_of_a_kind(dice):
        
        threesomes = list(filter((lambda value: dice.count(value) >= 3), dice))
        return threesomes[0] * Pips.THREE

    @staticmethod
    def four_of_a_kind(dice):
        
        quarter = []
        for value in dice:
            if dice.count(value) >= 4 and quarter.count(value) < 4:
                quarter.append(value)
        return sum(quarter)

    @staticmethod
    def small_straight(dice):

        for pip in Pips.minus(Pips.SIX):
            if dice.count(pip) != 1:
                return 0
        return Yatzy.chance(dice)

    @staticmethod
    def large_straight(dice):
        for pip in Pips.minus(Pips.ONE):
            if dice.count(pip) != 1:
                return 0
        return Yatzy.chance(dice)

    @staticmethod
    def full_house(dice):
        if Yatzy.score_pair(dice) and Yatzy.three_of_a_kind(dice):
            return Yatzy.chance(dice)
        else:
            return 0

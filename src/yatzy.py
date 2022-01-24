from calendar import c
from random import Random
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
        '''
        Applying set() to dice it deletes all repeated elements, 
        so if the returned list length is 1, indicates all 5 elements 
        where repeated and only contains one of this elements
        '''
        TOTAL_SCORE = 50
        JUST_ONE_ELEMENT = 1
        
        return TOTAL_SCORE if len(set(dice)) == JUST_ONE_ELEMENT else 0
    
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
        
        THREE = Pips.THREE.value
        threesomes = list(filter((lambda value: dice.count(value) >= THREE), dice))
                
        return threesomes[Pips.ONE.value] * THREE if len(threesomes) != 0 else 0
        

    @staticmethod
    def four_of_a_kind(dice):

        FOUR = Pips.FOUR.value
        quarters = list(filter((lambda value: dice.count(value) >= FOUR), dice))
        
        return quarters[Pips.ONE.value] * FOUR if len(quarters) != 0 else 0


    @staticmethod
    def small_straight(dice):

        ALL_PIPS = 5
        EXCLUDED_PIP = Pips.SIX.value
        
        return Yatzy.chance(filter((lambda pip: Yatzy.chance(dice) if EXCLUDED_PIP not in dice and len(set(dice)) == ALL_PIPS else 0), dice))

    @staticmethod
    def large_straight(dice):
        
        ALL_PIPS = 5
        EXCLUDED_PIP = Pips.ONE.value

        return Yatzy.chance(filter((lambda pip: Yatzy.chance(dice) if EXCLUDED_PIP not in dice and len(set(dice)) == ALL_PIPS else 0), dice))


    @staticmethod
    def full_house(dice):
        
        return Yatzy.chance(dice) if Yatzy.score_pair(dice) and Yatzy.three_of_a_kind(dice) else 0


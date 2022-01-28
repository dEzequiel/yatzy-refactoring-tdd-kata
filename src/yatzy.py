from src.pips import Pips
from src.values import Value

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
        return Value.TOTAL_SCORE if len(set(dice)) == Value.ONE else Value.ZERO
    
    @staticmethod
    def ones(dice):
        ONE_PIP = Pips.ONE.value
        return dice.count(ONE_PIP) * Value.ONE

    @staticmethod
    def twos(dice):
        TWO_PIP = Pips.TWO.value
        return dice.count(TWO_PIP) * Value.TWO

    @staticmethod
    def threes(dice):
        THREE_PIP = Pips.THREE.value
        return dice.count(THREE_PIP) * Value.THREE

    @staticmethod
    def fours(dice):
        FOUR_PIP = Pips.FOUR.value
        return dice.count(FOUR_PIP) * Value.FOUR

    @staticmethod
    def fives(dice):
        FIVE_PIP = Pips.FIVE.value
        return dice.count(FIVE_PIP) * Value.FIVE

    @staticmethod
    def sixes(dice):
        SIX_PIP = Pips.SIX.value
        return dice.count(SIX_PIP) * Value.SIX

    @staticmethod
    def score_pair(dice):
        for pip in Pips.reversed_values():
            if dice.count(pip) >= Value.TWO:
                return pip * Value.TWO
        return Value.ZERO

        # REVERSED_DICE = Pips.reversed_values()
        # return Yatzy.chance(filter((lambda pip: pip * TWO if REVERSED_DICE.count(pip) >= TWO else ZERO), REVERSED_DICE))

    @staticmethod
    def two_pair(dice):

        PAIRS_LIST = set(list(filter((lambda pip: dice.count(pip) >= Value.TWO), dice)))
        return sum(PAIRS_LIST) * Value.TWO if len(PAIRS_LIST) == Value.TWO else Value.ZERO

    @staticmethod
    def three_of_a_kind(dice):
        
        threesomes = list(filter((lambda value: dice.count(value) >= Value.THREE), dice))        
        return threesomes[Pips.ONE.value] * Value.THREE if len(threesomes) != Value.ZERO else Value.ZERO
        

    @staticmethod
    def four_of_a_kind(dice):

        quarters = list(filter((lambda value: dice.count(value) >= Value.FOUR), dice))        
        return quarters[Pips.ONE.value] * Value.FOUR if len(quarters) != Value.ZERO else Value.ZERO


    @staticmethod
    def small_straight(dice):

        EXCLUDED_PIP = Pips.SIX.value
        
        return Yatzy.chance(filter((lambda pip: Yatzy.chance(dice) if EXCLUDED_PIP not in dice and len(set(dice)) == Value.FIVE else Value.ZERO), dice))

    @staticmethod
    def large_straight(dice):
        
        EXCLUDED_PIP = Pips.ONE.value

        return Yatzy.chance(filter((lambda pip: Yatzy.chance(dice) if EXCLUDED_PIP not in dice and len(set(dice)) == Value.FIVE else Value.ZERO), dice))

    @staticmethod
    def full_house(dice):
        
        return Yatzy.chance(dice) if Yatzy.score_pair(dice) and Yatzy.three_of_a_kind(dice) else Value.ZERO


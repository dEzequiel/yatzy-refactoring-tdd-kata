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
        return dice.count(Pips.ONE.value) * Value.ONE

    @staticmethod
    def twos(dice):
        return dice.count(Pips.TWO.value) * Value.TWO

    @staticmethod
    def threes(dice):
        return dice.count(Pips.THREE.value) * Value.THREE

    @staticmethod
    def fours(dice):
        return dice.count(Pips.FOUR.value) * Value.FOUR

    @staticmethod
    def fives(dice):
        return dice.count(Pips.FIVE.value) * Value.FIVE

    @staticmethod
    def sixes(dice):
        return dice.count(Pips.SIX.value) * Value.SIX

    @staticmethod
    def score_pair(dice):
        # for pip in Pips.reversed_values():
        #     if dice.count(pip) >= Value.TWO:
        #         return pip * Value.TWO
        # return Value.ZERO

        REVERSED_DICE = Pips.reversed_values()
        
        return [a for a in REVERSED_DICE if dice.count(a) >= Value.TWO]
        print(x)
        
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

        return Yatzy.chance(filter((lambda pip: Yatzy.chance(dice) if Pips.SIX.value not in dice and len(set(dice)) == Value.FIVE else Value.ZERO), dice))

    @staticmethod
    def large_straight(dice):
        
        return Yatzy.chance(filter((lambda pip: pip if Pips.ONE.value not in dice and len(set(dice)) == Value.FIVE else Value.ZERO), dice))

    @staticmethod
    def full_house(dice):
        
        return Yatzy.chance(dice) if Yatzy.score_pair(dice) and Yatzy.three_of_a_kind(dice) else Value.ZERO


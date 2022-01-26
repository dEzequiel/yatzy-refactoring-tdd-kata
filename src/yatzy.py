from src.pips import Pips

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6

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
        
        return TOTAL_SCORE if len(set(dice)) == JUST_ONE_ELEMENT else ZERO
    
    @staticmethod
    def ones(dice):
        ONE_PIP = Pips.ONE.value
        return dice.count(ONE_PIP) * ONE

    @staticmethod
    def twos(dice):
        TWO_PIP = Pips.TWO.value
        return dice.count(TWO_PIP) * TWO

    @staticmethod
    def threes(dice):
        THREE_PIP = Pips.THREE.value
        return dice.count(THREE_PIP) * THREE

    @staticmethod
    def fours(dice):
        FOUR_PIP = Pips.FOUR.value
        return dice.count(FOUR_PIP) * FOUR

    @staticmethod
    def fives(dice):
        FIVE_PIP = Pips.FIVE.value
        return dice.count(FIVE_PIP) * FIVE

    @staticmethod
    def sixes(dice):
        SIX_PIP = Pips.SIX.value
        return dice.count(SIX_PIP) * SIX

    @staticmethod
    def score_pair(dice):
        PAIR = 2
        for pip in Pips.reversed_values():
            if dice.count(pip) >= 2:
                return pip * PAIR
        return 0

    @staticmethod
    def two_pair(dice):

        TWO = 2
        PAIR_LIST = set(list(filter((lambda pip: dice.count(pip) >= TWO), dice)))
        
        return sum(PAIR_LIST) * TWO if len(PAIR_LIST) == TWO else 0

    @staticmethod
    def three_of_a_kind(dice):
        
        threesomes = list(filter((lambda value: dice.count(value) >= THREE), dice))        
        return threesomes[Pips.ONE.value] * THREE if len(threesomes) != 0 else 0
        

    @staticmethod
    def four_of_a_kind(dice):

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


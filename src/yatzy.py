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
    
    @classmethod
    def calculate_one_pair(cls, dice):
        return set(list(filter((lambda pip: dice.count(pip) >= Value.TWO), Pips.reversed_values())))
    
    @classmethod
    def score_pair(cls, dice):
        return max(cls.calculate_one_pair(dice)) * Value.TWO if len(cls.calculate_one_pair(dice)) != Value.ZERO else Value.ZERO
    
    @classmethod
    def calculate_two_pairs(cls, dice):
        return set(list(filter((lambda pip: dice.count(pip) >= Value.TWO), dice)))
        
    @classmethod
    def two_pair(cls, dice):
        return sum(cls.calculate_two_pairs(dice)) * Value.TWO if len(cls.calculate_two_pairs(dice)) == Value.TWO else Value.ZERO

    @classmethod
    def number_of_a_kind(cls, dice, value):
        return set((list(filter((lambda pip: dice.count(pip) >= value), dice))))
    
    @classmethod
    def three_of_a_kind(cls, dice):
        return max(cls.number_of_a_kind(dice, Pips.THREE.value)) * Value.THREE if len(cls.number_of_a_kind(dice, Pips.THREE.value)) != Value.ZERO else Value.ZERO
        
    @classmethod
    def four_of_a_kind(cls, dice):
        return max(cls.number_of_a_kind(dice, Pips.FOUR.value)) * Value.FOUR if len(cls.number_of_a_kind(dice, Pips.FOUR.value)) != Value.ZERO else Value.ZERO

    @staticmethod
    def small_straight(dice):
        return Yatzy.chance(filter((lambda pip: Yatzy.chance(dice) if Pips.SIX.value not in dice and len(set(dice)) == Value.FIVE else Value.ZERO), dice))

    @staticmethod
    def large_straight(dice):
        return Yatzy.chance(filter((lambda pip: pip if Pips.ONE.value not in dice and len(set(dice)) == Value.FIVE else Value.ZERO), dice))

    @staticmethod
    def full_house(dice):
        return Yatzy.chance(dice) if Yatzy.score_pair(dice) and Yatzy.three_of_a_kind(dice) else Value.ZERO


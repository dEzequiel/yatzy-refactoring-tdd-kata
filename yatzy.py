class Yatzy:
    
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(dice):

        total = 0
        for value in dice:
            total += value
        return total

    @staticmethod
    def yatzy(dice):

        comparing_number = dice[0]
        for value in dice:
            if comparing_number != dice[value]:
                return 0
        return 50

    @staticmethod
    def ones(dice):
        ONE = 1
        total_count = dice.count(ONE)
        return total_count * ONE

    @staticmethod
    def twos(dice):
        TWO = 2
        total_count = dice.count(TWO)
        return total_count * TWO

    @staticmethod
    def threes(dice):
        THREE = 3
        total_count = dice.count(THREE)
        return total_count * THREE

    @staticmethod
    def fours(dice):
        FOUR = 4
        total_count = dice.count(FOUR)
        return total_count * FOUR

    @staticmethod
    def fives(dice):
        FIVE = 5
        total_count = dice.count(FIVE)
        return total_count * FIVE

    @staticmethod
    def sixes(dice):
        SIX = 6
        total_count = dice.count(SIX)
        return total_count * SIX

    @staticmethod
    def score_pair(dice):
        max_value = max(dice)
        if dice.count(max_value) == 2:
            return max_value * 2
        else:
            for value in dice:
                if dice.count(value) == 2:
                    return value * 2
                else:
                    return 0

    @staticmethod
    def two_pair(dice):

        repeated = []
        for value in dice:
            if dice.count(value) >= 2:
                repeated.append(value)

        no_repeats = list(dict.fromkeys(repeated))

        sumatory = [value * 2 for value in no_repeats]

        return Yatzy.chance(sumatory)

    @staticmethod
    def three_of_a_kind(dice):
        
        trio = []
        for value in dice:
            if dice.count(value) >= 3 and trio.count(value) < 3:
               trio.append(value)
        return sum(trio)

    @staticmethod
    def four_of_a_kind(dice):
        
        quarter = []
        for value in dice:
            if dice.count(value) >= 4 and quarter.count(value) < 4:
                quarter.append(value)
        return sum(quarter)

    @staticmethod
    def small_straight(dice):

        for i in range(1, 6):
            if dice.count(i) != 1:
                return 0
        return sum(dice)

    @staticmethod
    def large_straight(dice):

        for i in range(2, 7):
            if dice.count(i) != 1:
                return 0
        return Yatzy.chance(dice)

    @staticmethod
    def full_house(dice):

        if Yatzy.two_pair(dice) and Yatzy.three_of_a_kind(dice):
            return Yatzy.chance(dice)
        else:
            return 0

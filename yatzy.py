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
        counter = dice.count(1)
        return counter * 1

    @staticmethod
    def twos(dice):
        counter = dice.count(2)
        return counter * 2

    @staticmethod
    def threes(dice):
        counter = dice.count(3)
        return counter * 3

    @staticmethod
    def fours(dice):
        counter = dice.count(4)
        return counter * 4

    @staticmethod
    def fives(dice):
        counter = dice.count(5)
        return counter * 5

    @staticmethod
    def sixes(dice):
        counter = dice.count(6)
        return counter * 6

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
        for i in dice:
            if dice.count(i) >= 2:
                repeated.append(i)

        no_repeats = list(dict.fromkeys(repeated))

        sumatory = [x * 2 for x in no_repeats]

        return Yatzy.chance(sumatory)

    @staticmethod
    def three_of_a_kind(dice):
        
        trio = []
        for i in dice:
            if dice.count(i) >= 3 and trio.count(i) < 3:
               trio.append(i)
        return sum(trio)

    @staticmethod
    def four_of_a_kind(dice):
        
        quarter = []
        for i in dice:
            if dice.count(i) >= 4 and quarter.count(i) < 4:
                quarter.append(i)
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

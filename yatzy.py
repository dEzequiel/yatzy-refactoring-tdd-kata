from typing import SupportsAbs


class Yatzy:
    def __init__(self, dice):
        self.dice = list(dice)

    @staticmethod
    def chance(dice):

        total = 0
        for value in dice:
            total += value
        return total

    @staticmethod
    def yatzy(dice):
        check = True
        for value in dice:
            if dice[0] != dice[value]:
                check = False
                break
        if check == True:
            return 50
        else:
            return 0

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

    # metodo de instancia
    def fours(self):
        counter = self.dice.count(4)
        return counter * 4

    def fives(self):
        counter = self.dice.count(5)
        return counter * 5

    def sixes(self):
        counter = self.dice.count(6)
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

        return sum(sumatory)

    @staticmethod
    def four_of_a_kind(dice):

        for i in dice:
            if dice.count(i) == 4:
                return i * 4

            return 0

    @staticmethod
    def three_of_a_kind(dice):

        for i in dice:
            if dice.count(i) == 3:
                return i * 3
        return 0

    @staticmethod
    def small_straight(dice):

        # Generates an already sorted list to compare with given list.
        lista = []
        for n in range(1, 6):
            lista.append(n)

        if dice == lista:
            return 15
        else:
            return 0

    @staticmethod
    def large_straight(dice):

        for i in range(2, 7):
            if dice.count(i) != 1:  # If number appear more than one, is not a sequence.
                return 0

        return Yatzy.chance(dice)

    # @staticmethod
    # def full_house(dice):
    #     two = Yatzy.two_pair(dice)
    #     three = Yatzy.three_of_a_kind(dice)

    #     print(two)
    #     print(three)

    #     if two and three:
    #         return two + three
    #     else:
    #         return 0

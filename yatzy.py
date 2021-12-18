from typing import Dict, NoReturn


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
                break;
        if (check == True): return 50
        else: return 0
    
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
        
        pairs = []
        for value in dice:
            if dice.count(value) == 2:
                pairs.append(value)
        
        if len(pairs) == 1:
            return 0
        
        pairs.pop()
        pairs.pop(0)
        
        sum = 0
        print(pairs)
        for value in pairs:
            sum += value * 2
        
        return sum
                       
            
            
    
    @staticmethod
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
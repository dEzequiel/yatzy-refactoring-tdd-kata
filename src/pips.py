from enum import Enum, unique

@unique
class Pips(Enum):

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @classmethod
    def values(cls):
        return [number.value for number in Pips.__members__.values()]
    
    @classmethod
    def minus(cls, pip):
        return set(cls.values()) - {pip.value}
    
    @classmethod
    def reversed_values(cls):
        return reversed(cls.values())
    
if __name__ == '__main__':
    pass

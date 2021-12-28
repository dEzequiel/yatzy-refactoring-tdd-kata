import unittest
from yatzy import *


class YatzyUnitTesting(unittest.TestCase):
    def test_chance(self):
        yatzy_result = Yatzy.chance([1, 2, 3, 4, 5])
        self.assertEqual(yatzy_result, 15)

    def test_yatzy(self):
        yatzy_result = Yatzy.yatzy([1, 1, 1, 1, 1])
        self.assertEqual(yatzy_result, 50)


if __name__ == "__main_:":
    unittest.main()

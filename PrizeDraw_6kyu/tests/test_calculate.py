from unittest import TestCase
from PrizeDraw.code.prize_draw_6kyu import calculate


class TestCalculate(TestCase):
    def test_calculate_LenZeroIsZero(self):
        self.assertEqual(0, calculate("", 2))

    def test_calculate_FirstNameIsSumOfLengthAndCharRankXWeight(self):
        self.assertEqual(108, calculate("Paul", 2))

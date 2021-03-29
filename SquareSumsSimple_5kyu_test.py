from unittest import TestCase
from SquareSumsSimple_5kyu import square_sums_row


class TestSquareSumsRow(TestCase):
    def test_TrueCases(self):
        for i in [15, 23, 25, 31]:
            actual = square_sums_row(i)
            print(i, actual)

            # a = actual[:-1]
            # b = actual[1:]
            # for x in zip(a, b):
            #     if sum(x) ** .5 % 1:
            #         self.assertFalse(0, 'sums of adjacent numbers should be squares')
            #         return

            actual.sort()
            self.assertEquals(actual, list(range(1, i + 1)), 'missing numbers')

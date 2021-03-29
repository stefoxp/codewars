from unittest import TestCase
from DirectionsReduction_5kyu import dirReduc


class TestDirReduc(TestCase):
    def test_SimpleReduction(self):
        self.assertEquals(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]),
                          ['WEST'])

from unittest import TestCase
from JohnAnnSignUpCodewars_5kyu import john, ann, sum_john, sum_ann


class TestJohnAndAnn(TestCase):
    def test_JohnBasic(self):
        self.assertEquals(john(11), [0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6])

    def test_AnnBasic(self):
        self.assertEquals(ann(6), [1, 1, 2, 2, 3, 3])

    def test_SumJohnBasic(self):
        self.assertEquals(sum_john(75), 1720)

    def test_SumAnnBasic(self):
        self.assertEquals(sum_ann(115), 4070)

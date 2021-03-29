from unittest import TestCase
from PrizeDraw.code.prize_draw_6kyu import reverse_order


class TestOrder(TestCase):
    def test_order(self):
        self.assertEqual([200, 190, 150],
                         reverse_order([150, 190, 200]))

    def test_order_withDuplicatedRanks(self):
        self.assertEqual([200, 190, 190, 150],
                         reverse_order([150, 190, 190, 200]))

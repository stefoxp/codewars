from unittest import TestCase
from FindTheSmallest_5kyu import smallest


class TestSmallest(TestCase):
    def test_261235is126235_2_0(self):
        self.assertEquals(smallest(261235), [126235, 2, 0])
        # self.assertEquals(smallest(285365), [238565, 3, 1])
        # self.assertEquals(smallest(269045), [26945, 3, 0])
        # self.assertEquals(smallest(296837), [239687, 4, 1])

    def test_209917is29917_0_1(self):
        self.assertEquals(smallest(209917), [29917, 0, 1])

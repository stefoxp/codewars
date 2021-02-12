from unittest import TestCase
from ByState_6kyu import by_state


class TestByState(TestCase):
    def test_Basic(self):
        case0 = """John Daggett, 341 King Road, Plymouth MA
        Alice Ford, 22 East Broadway, Richmond VA
        Sal Carpenter, 73 6th Street, Boston MA"""
        answer = "Massachusetts\r\n..... John Daggett 341 King Road Plymouth Massachusetts\r\n..... " \
                 "Sal Carpenter 73 6th Street Boston Massachusetts\r\n Virginia\r\n..... " \
                 "Alice Ford 22 East Broadway Richmond Virginia"

        self.assertEquals(answer, by_state(case0))

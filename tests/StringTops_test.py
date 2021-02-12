from unittest import TestCase
from StringTops_6kyu import tops


class TestTops(TestCase):
    def test_topsEmptyIsEmpty(self):
        self.assertEquals(tops(""), "")

    def test_tops12Is2(self):
        self.assertEquals(tops("12"), "2")

    def test_tops_abcdefghijklmnopqrstuvwxyz12345(self):
        self.assertEquals(tops("abcdefghijklmnopqrstuvwxyz12345"), "3pgb")

    def test_tops_abcd123ABC(self):
        self.assertEquals(tops("abcdefghijklmnopqrstuvwxyz1236789ABCDEFGHIJKLMN"), "M3pgb")

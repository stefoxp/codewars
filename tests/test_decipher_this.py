from unittest import TestCase
from DecipherThis_6kyu import decipher_this


class TestDecipherThis(TestCase):
    def test_decipher_this_72IsH(self):
        self.assertEquals(decipher_this('72'), 'H')

    def test_decipher_this_72oIsHo(self):
        self.assertEquals(decipher_this('72o'), 'Ho')

    def test_decipher_this_72olleIsHello(self):
        self.assertEquals(decipher_this('72olle'), 'Hello')

    # def test_decipher_this(self):
    #     self.assertEquals(decipher_this('72olle 103doo 100ya'), 'Hello good day')

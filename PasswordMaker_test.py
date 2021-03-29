from unittest import TestCase
from PasswordMaker_7kyu import make_password


class TestMakePassword(TestCase):
    def test_GiveIsGml0gmd(self):
        self.assertEquals(make_password("Give me liberty or give me death"),
                          "Gml0gmd",
                          "Wrong output for 'Give me liberty or give me death'")
        self.assertEquals(make_password("Keep Calm and Carry On"),
                          "KCaC0",
                          "Wrong output for 'Keep Calm and Carry On'")

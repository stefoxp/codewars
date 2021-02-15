from unittest import TestCase
from PlayingWithPassphrases.code.play import play_pass


class TestPlayPass(TestCase):
    def test_play_pass_BisC(self):
        self.assertEqual("!4897 Oj oSpC",
                         play_pass("BORN IN 2015!", 1))
        self.assertEqual("!!!vPz fWpM J",
                         play_pass("I LOVE YOU!!!", 1))
        self.assertEqual(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2),
                         "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")

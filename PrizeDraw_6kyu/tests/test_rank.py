from unittest import TestCase
from PrizeDraw.code.prize_draw_6kyu import rank


class TestRank(TestCase):
    def test_rank_LenZeroIsNoParticipants(self):
        self.assertEqual("No participants", rank("", "", 1))

    def test_rank_LenLessThanNIsNotEnoughParticipants(self):
        self.assertEqual("Not enough participants", rank("ciao,bao", "", 3))

    # def test_rank_LenMoreThanNIsValoreCalcolato(self):
    #    self.assertEqual("valore calcolato", rank("ciao,bao,mitico", "", 3))

    def test_rank_ExampleValues(self):
        self.assertEqual("PauL", rank("COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH", [1, 4, 4, 5, 2, 1], 4))
        self.assertEqual("Lagon", rank("Lagon,Lily", [1, 5], 2))
        self.assertEqual("Not enough participants",
                         rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8))

from unittest import TestCase
from MovesInSquaredStrings01_7kyu import vert_mirror, hor_mirror, oper


class TestVertMirror(TestCase):
    def test_BasicVert(self):
        self.assertEquals(vert_mirror("hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"),
                          "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")
        self.assertEquals(vert_mirror("IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"),
                          "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP")


class TestHorMirror(TestCase):
    def test_BasicHor(self):
        self.assertEquals(hor_mirror("lVHt\nJVhv\nCSbg\nyeCt"),
                          "yeCt\nCSbg\nJVhv\nlVHt")
        self.assertEquals(hor_mirror("njMK\ndbrZ\nLPKo\ncEYz"),
                          "cEYz\nLPKo\ndbrZ\nnjMK")


class TestOperMirror(TestCase):
    def test_BasicOper(self):
        self.assertEquals(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"),
                          "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")
        self.assertEquals(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"),
                          "yeCt\nCSbg\nJVhv\nlVHt")
        """
        testing(oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"),
                "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP")

        testing(oper(hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz"), "cEYz\nLPKo\ndbrZ\nnjMK")
        """
from unittest import TestCase
from MovesInSquaredStrings03_6kyu import rot_90_clock, diag_1_sym, selfie_and_diag1, oper


class TestRot90Clock(TestCase):
    def test_basic(self):
        self.assertEquals(rot_90_clock("abcd\nefgh\nijkl\nmnop"),
                          "miea\nnjfb\nokgc\nplhd")
        self.assertEquals(rot_90_clock("rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb"),
                          "Sixdvr\ndJNCGg\nmBWhca\nEYgZEv\nKDXVKc\nbORWle")


class TestDiag1Sym(TestCase):
    def test_basic(self):
        self.assertEquals(diag_1_sym("abcd\nefgh\nijkl\nmnop"),
                          "aeim\nbfjn\ncgko\ndhlp")
        self.assertEquals(diag_1_sym("wuUyPC\neNHWxw\nehifmi\ntBTlFI\nvWNpdv\nIFkGjZ"),
                          "weetvI\nuNhBWF\nUHiTNk\nyWflpG\nPxmFdj\nCwiIvZ")


class TestSelfAndDiag(TestCase):
    def test_basic(self):
        self.assertEquals(selfie_and_diag1("NJVGhr\nMObsvw\ntPhCtl\nsoEnhi\nrtQRLK\nzjliWg"),
                          "NJVGhr|NMtsrz\nMObsvw|JOPotj\ntPhCtl|VbhEQl\nsoEnhi|GsCnRi\nrtQRLK|hvthLW\nzjliWg|rwliKg")


class TestOper(TestCase):
    def test_basic(self):
        self.assertEquals(oper(diag_1_sym, "abcd\nefgh\nijkl\nmnop"),
                          "aeim\nbfjn\ncgko\ndhlp")

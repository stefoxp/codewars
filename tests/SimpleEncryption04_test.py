from unittest import TestCase
from SimpleEncryption04_5kyu import decrypt, encrypt


class TestDecrypt(TestCase):
    def test_A111IsS(self):
        self.assertEquals(decrypt("S", 111),
                          "A")
        self.assertEquals(decrypt("s", 111),
                          "a")


class TestEncrypt(TestCase):
    def test_A111IsS(self):
        self.assertEquals(encrypt("A", 111),
                          "S")
        self.assertEquals(encrypt("a", 111),
                          "s")

    def test_Abc212IsSmb(self):
        self.assertEquals(encrypt("Abc", 212),
                          "Smb")

    def test_Wave345IsTgDotY(self):
        self.assertEquals(encrypt("Wave", 345),
                          "Tg.y")

    def test_This348IsIaqh(self):
        self.assertEquals(encrypt("This is a test.", 348),
                          "Iaqh qh g iyhi,")

    def test_TrueCaseIsOk(self):
        self.assertEquals(
            encrypt("Do the kata Kobayashi Maru Test. Endless fun and excitement when finding a solution.", 583),
            "Sr pgi jlpl Jr,lqlage Zlow Piapc I.skiaa dw. l.s ibnepizi.p ugi. de.se.f l arkwper.c")

    def test_BallIsMoreGff(self):
        self.assertEquals(encrypt("Ball", 444),
                          ">gff")

    def test_Text0IsText(self):
        self.assertEquals(encrypt("Wave", 0),
                          "Wave")

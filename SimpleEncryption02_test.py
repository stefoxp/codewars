from unittest import TestCase
from SimpleEncryption02IndexDifference_5kyu import decrypt, encrypt, step_1, step_2, step_3, step_2_dec
import string


class TestDecrypt(TestCase):
    def setUp(self):
        self.vocabulary = string.ascii_uppercase + string.ascii_lowercase + string.digits + ".,:;-?! '()$%&" + '"'

    def test_EmptyIsEmpty(self):
        self.assertEquals(
            decrypt(""),
            "")

    def test_NullIsNull(self):
        self.assertEquals(
            decrypt(None),
            None)

    def test_Step2Dec(self):
        self.assertEquals(
            step_2_dec("B61kujla"),
            list("BUsInEsS"))

    def test_TrueCaseIsOk(self):
        self.assertEquals(
            decrypt("$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w"),
            "Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement when finding a solution!")


class TestEncrypt(TestCase):
    def setUp(self):
        self.vocabulary = string.ascii_uppercase + string.ascii_lowercase + string.digits + ".,:;-?! '()$%&" + '"'

    def test_EmptyIsEmpty(self):
        self.assertEquals(
            encrypt(""),
            "")

    def test_NullIsNull(self):
        self.assertEquals(
            encrypt(None),
            None)

    def test_CharUnknownIsException(self):
        self.assertRaises(Exception, encrypt, "b@e")

    def test_Step1(self):
        self.assertEquals(
            step_1(list("Business")),
            list("BUsInEsS"))

    def test_Step2(self):
        self.assertEquals(
            step_2("BUsInEsS"),
            list("B61kujla"))

    def test_Step3(self):
        self.assertEquals(
            step_3(list("B61kujla")),
            list("&61kujla"))

    def test_TrueCaseIsOk(self):
        self.assertEquals(
            encrypt("Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement when finding a solution!"),
            "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w")

from unittest import TestCase
from SimpleEncryption01AlternatingSplit_6kyu import decrypt, encrypt


class TestDecrypt(TestCase):
    def test_NullIsNull(self):
        self.assertEquals(decrypt("", 0), "")

    def test_NoneIsNone(self):
        self.assertEquals(decrypt(None, 0), None)

    def test_ThisZeroIsThis(self):
        self.assertEquals(decrypt("This is a test!", 0), "This is a test!")

    def test_HsiOneIsThis(self):
        self.assertEquals(decrypt("hsi  etTi sats!", 1), "This is a test!")

    def test_S_eTTwoIsThis(self):
        self.assertEquals(decrypt("s eT ashi tist!", 2), "This is a test!")

    def test_VariousMoreThanOneIsThis(self):
        self.assertEquals(encrypt("This is a test!", 3), " Tah itse sits!")
        self.assertEquals(encrypt("This is a test!", 4), "This is a test!")
        self.assertEquals(encrypt("This is a test!", -1), "This is a test!")
        self.assertEquals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")


class TestEncrypt(TestCase):
    def test_NullIsNull(self):
        self.assertEquals(encrypt("", 0), "")

    def test_NoneIsNone(self):
        self.assertEquals(encrypt(None, 0), None)

    def test_ThisZeroIsThis(self):
        self.assertEquals(encrypt("This is a test!", 0), "This is a test!")

    def test_ThisOneIsHsi(self):
        self.assertEquals(encrypt("This is a test!", 1), "hsi  etTi sats!")

    def test_ThisTwoIsS_eT(self):
        self.assertEquals(encrypt("This is a test!", 2), "s eT ashi tist!")

    def test_ThisMoreThanOneIsVarious(self):
        self.assertEquals(encrypt("This is a test!", 3), " Tah itse sits!")
        self.assertEquals(encrypt("This is a test!", 4), "This is a test!")
        self.assertEquals(encrypt("This is a test!", -1), "This is a test!")
        self.assertEquals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")



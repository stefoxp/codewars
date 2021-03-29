from unittest import TestCase
from EncryptThis_6kyu import encrypt_this


class TestEncryptThis(TestCase):
    def setUp(self):
        self.tests = [
            ("", ""),
            ("A wise old owl lived in an oak", "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
            ("The more he saw the less he spoke", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
            ("The less he spoke the more he heard", "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
            ("Why can we not all be like that wise old bird",
             "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
            ("Thank you Piotr for all your help", "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
        ]

    def test_encrypt_this_EmptyIsEmpty(self):
        self.assertEquals(encrypt_this(""), "")

    def test_encrypt_this_AIs(self):
        self.assertEquals(encrypt_this("A"), "65")

    def test_encrypt_this_AbIs(self):
        self.assertEquals(encrypt_this("Ab"), "65b")

    def test_encrypt_this_HelloIs72olle(self):
        self.assertEquals(encrypt_this("Hello"), "72olle")

    def test_encrypt_this_goodIs103doo(self):
            self.assertEquals(encrypt_this("good"), "103doo")

    def test_encrypt_this_hello_worldIs104olle_119drlo(self):
            self.assertEquals(encrypt_this("hello  world"), "104olle 119drlo")

    # def test_encrypt_this_A_wise_old_owl_lived_in_an_oakIs65_119esi_111dl_111lw_108dvei_105n_97n_111ka(self):
    #         self.assertEquals(encrypt_this("A wise old owl lived in an oak"),
    #                           "65 119esi 111dl 111lw 108dvei 105n 97n 111ka")

    def test_encrypt_this(self):
        for t in self.tests:
            inp, exp = t
            self.assertEquals(encrypt_this(inp), exp)

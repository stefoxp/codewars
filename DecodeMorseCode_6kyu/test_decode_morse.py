from unittest import TestCase
from decode_morse import decodeMorse

class TestDecodeMorse(TestCase):
    def test_decode_morse_single_letter(self):
        self.assertEqual(decodeMorse(".-"), "A")
        self.assertEqual(decodeMorse("--.-"), "Q")
        self.assertEqual(decodeMorse(".----"), "1")

    def test_decode_morse_phrase(self):
        self.assertEqual(decodeMorse(".... . -.--   .--- ..- -.. ."), "HEY JUDE")

    def test_decode_morse_extra_spaces_before_ignore(self):
        self.assertEqual(decodeMorse(" .... . -.--"), "HEY")
        self.assertEqual(decodeMorse("     .... . -.--"), "HEY")

    def test_decode_morse_extra_spaces_after_ignore(self):
        self.assertEqual(decodeMorse(".... . -.--       "), "HEY")

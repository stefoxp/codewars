from unittest import TestCase
from FirstNonRepeatingCharacter_5kyu import first_non_repeating_letter


class TestFirstNonRepeatingLetter(TestCase):
    def test_SingleCharIsChar(self):
        self.assertEquals("a", first_non_repeating_letter("a"))
        self.assertEquals("#", first_non_repeating_letter("#"))

    def test_FirstNonRepeatingCharIsThisChar(self):
        self.assertEquals("t", first_non_repeating_letter("stress"))
        self.assertEquals("e", first_non_repeating_letter("moonmen"))

    def test_EmptyIsEmpty(self):
        self.assertEquals("", first_non_repeating_letter(""))

    def test_AllRepeatingIsEmpty(self):
        self.assertEquals("", first_non_repeating_letter("aa"))
        self.assertEquals("", first_non_repeating_letter("abba"))

    def test_OddCharIsFirstCharNonRepeating(self):
        self.assertEquals("#", first_non_repeating_letter("~><#~><"))
        self.assertEquals("w", first_non_repeating_letter("hello world, eh?"))

    def test_HandleLetterCases(self):
        self.assertEquals("T", first_non_repeating_letter("sTreSS"))
        self.assertEquals(",", first_non_repeating_letter("Go hang a salami, I\'m a lasagna hog!"))

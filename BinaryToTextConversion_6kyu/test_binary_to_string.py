from unittest import TestCase
from binary_to_string import binary_to_string


class TestBinaryToString(TestCase):
    def test_btos_empty_is_empty(self):
        self.assertEqual(binary_to_string(""), "")

    def test_btos_eight_bits_is_one_char(self):
        self.assertEqual(binary_to_string("00110001"), "1")

    def test_btos_each_eight_bits_is_one_char(self):
        self.assertEqual(binary_to_string("0100100001100101011011000110110001101111"), "Hello")
        self.assertEqual(binary_to_string('00110001001100000011000100110001'), '1011')

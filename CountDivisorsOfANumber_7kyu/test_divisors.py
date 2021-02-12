from unittest import TestCase
from divisors import divisors

class TestDivisors(TestCase):
    def test_divisors_of_one_is_one(self):
        self.assertEqual(divisors(1), 1)

    def test_divisors_of_two_is_two(self):
        self.assertEqual(divisors(2), 2)

    def test_divisors_of_three_is_two(self):
        self.assertEqual(divisors(3), 2)

    def test_divisors_of_four_is_two(self):
        self.assertEqual(divisors(4),3)

'''
Test.assert_equals(divisors(4), 3)
Test.assert_equals(divisors(5), 2)
Test.assert_equals(divisors(12), 6)
Test.assert_equals(divisors(30), 8)
Test.assert_equals(divisors(4096), 13)
'''
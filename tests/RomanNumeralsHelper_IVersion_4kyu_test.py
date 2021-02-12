import unittest
from RomanNumeralsHelper_IVersion_4kyu import RomanNumerals


class TestToI(unittest.TestCase):
    def testOneIsI(self):
        self.assertEqual('I', RomanNumerals.to_i(1))

    def testTenIsIIIIIIIIII(self):
        self.assertEqual('IIIIIIIIII', RomanNumerals.to_i(10))


class TestToRoman(unittest.TestCase):
    def testOneIsI(self):
        self.assertEqual('I', RomanNumerals.to_roman(1))

    def testThousandIsM(self):
        self.assertEqual('M', RomanNumerals.to_roman(1000))

    def testFourIsIV(self):
        self.assertEqual('IV', RomanNumerals.to_roman(4))

    def test1990IsMCMXC(self):
        self.assertEqual('MCMXC', RomanNumerals.to_roman(1990))

    def test2008IsMMVIII(self):
        self.assertEqual('MMVIII', RomanNumerals.to_roman(2008))


class TestFromRoman(unittest.TestCase):
    def testIIsOne(self):
        self.assertEqual(1, RomanNumerals.from_roman('I'))

    def testMIsThousand(self):
        self.assertEqual(1000, RomanNumerals.from_roman('M'))

    def testMCMXCIs1990(self):
        self.assertEqual(1990, RomanNumerals.from_roman("MCMXC"))

    def testMMVIIIIs2008(self):
        self.assertEqual(2008, RomanNumerals.from_roman("MMVIII"))


if __name__ == '__main__':
    unittest.main()

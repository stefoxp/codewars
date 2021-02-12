"""
Task

Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
Examples

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000

Help
Symbol 	Value
I 	1
V 	5
X 	10
L 	50
C 	100
D 	500
M 	1000
"""
"""TODO: create a RomanNumerals helper object"""


class RomanNumerals:
    conversion = (('M', 1000),
                  ('CM', 900),
                  ('D', 500),
                  ('CD', 400),
                  ('C', 100),
                  ('XC', 90),
                  ('L', 50),
                  ('XL', 40),
                  ('X', 10),
                  ('IX', 9),
                  ('V', 5),
                  ('IV', 4),
                  ('I', 1))

    @staticmethod
    def to_i(number):
        result = ""

        for i in range(number):
            result += "I"

        return result

    @staticmethod
    def to_roman(numeral):
        result = RomanNumerals.to_i(numeral)

        for c in RomanNumerals.conversion:
            result = result.replace(RomanNumerals.to_i(c[1]), c[0])

        return result

    @staticmethod
    def from_roman(roman):
        result = 0

        for c in RomanNumerals.conversion:
            if len(c[0]) == 2:
                if c[0] in roman:
                    result += c[1]
                    roman = roman.replace(c[0], "")

        for letter in roman:
            for c in RomanNumerals.conversion:
                if c[0] == letter:
                    result += c[1]

        return result


# TODO: Replace examples and use TDD development by writing your own tests
# These are some of the methods available:
#   test.expect(boolean, [optional] message)
#   test.assert_equals(actual, expected, [optional] message)
#   test.assert_not_equals(actual, expected, [optional] message)

# You can use Test.describe and Test.it to write BDD style test groupings


"""
Test.describe('Sample Tests')

test.assert_equals(RomanNumerals.to_roman(1000), 'M')
test.assert_equals(RomanNumerals.from_roman('M'), 1000)
"""

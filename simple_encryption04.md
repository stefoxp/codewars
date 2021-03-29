# SimpleEncryption04

## Task

You have to write two methods to encrypt and decrypt strings.
Both methods have two parameters:

1. The string to encrypt/decrypt
2. The Qwerty-Encryption-Key (000-999)

The rules are very easy:

The crypting-regions are these 3 lines from your keyboard:

1. "qwertyuiop"
2. "asdfghjkl"
3. "zxcvbnm,."

If a char of the string is not in any of these regions, take the char direct in the output.
If a char of the string is in one of these regions: Move it by the part of the key in the
region and take this char at the position from the region.
If the movement is over the length of the region, continue at the beginning.
The encrypted char must have the same case like the decrypted char!
So for upperCase-chars the regions are the same, but with pressed "SHIFT"!

The Encryption-Key is an integer number from 000 to 999. E.g.: 127

The first digit of the key (e.g. 1) is the movement for the first line.
The second digit of the key (e.g. 2) is the movement for the second line.
The third digit of the key (e.g. 7) is the movement for the third line.

(Consider that the key is an integer! When you got a 0 this would mean 000. A 1 would mean 001. And so on.)

You do not need to do any prechecks. The strings will always be not null and will always have a length > 0. You do not have to throw any exceptions.

## An Example

Encrypt "Ball" with key 134

1. "B" is in the third region line. Move per 4 places in the region. -> ">" (Also "upperCase"!)
2. "a" is in the second region line. Move per 3 places in the region. -> "f"
3. "l" is in the second region line. Move per 3 places in the region. -> "d"
4. "l" is in the second region line. Move per 3 places in the region. -> "d"
--> Output would be ">fdd"

**Hint**: Don't forget: The regions are from an US-Keyboard!
In doubt google for "US Keyboard."

This kata is part of the Simple Encryption Series:
Simple Encryption #1 - Alternating Split
Simple Encryption #2 - Index-Difference
Simple Encryption #3 - Turn The Bits Around
Simple Encryption #4 - Qwerty

Have fun coding it and please don't forget to vote and rank this kata! :-)

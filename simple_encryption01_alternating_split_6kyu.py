"""
For building the encrypted string:
Take every 2nd char from the string,
then the other chars, that are not every 2nd char,
and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.
"""


def decrypt(encrypted_text, n):
    result = encrypted_text

    if n > 0:
        for num in range(n):
            result = de_substitute(list(result))

    return result


def de_substitute(encrypted_text):
    sx = encrypted_text[:int(len(encrypted_text) / 2)]
    result = encrypted_text[int(len(encrypted_text) / 2):]

    offset = 0

    for i in range(len(encrypted_text)):
        if i % 2 != 0:
            result.insert(i, sx[offset])
            offset += 1

    return ''.join(result)


def encrypt(text, n):
    result = text

    if n > 0:
        for num in range(n):
            result = substitute(list(result))

    return result


def substitute(text):
    result = ""

    for i in range(1, len(text), 2):
        result += text[i]
        text[i] = ""

    for x in text:
        result += x

    return result

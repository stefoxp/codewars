"""
One suggestion to build a satisfactory password is to start with a memorable phrase or sentence
and make a password by extracting the first letter of each word.

Even better is to replace some of those letters with numbers (e.g., the letter O can be replaced with the number 0):

    instead of including i or I put the number 1 in the password;
    instead of including o or O put the number 0 in the password;
    instead of including s or S put the number 5 in the password.

Examples:

"Give me liberty or give me death"  --> "Gml0gmd"
"Keep Calm and Carry On"            --> "KCaC0"

"""


def make_password(phrase):
    result = ""
    a = phrase.split(" ")

    substitutes = (
        ("o", "0"),
        ("O", "0"),
        ("i", "1"),
        ("I", "1"),
        ("s", "5"),
        ("S", "5")
    )

    for word in a:
        result += word[0]

    for s in substitutes:
        result = result.replace(s[0], s[1])

    return result

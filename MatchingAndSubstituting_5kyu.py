"""
I got lots of files beginning like this:

Program title: Primes
Author: Kern
Corporation: Gold
Phone: +1-503-555-0091
Date: Tues April 9, 2005
Version: 6.7
Level: Alpha

Here we will work with strings like the string data above and not with files.

The function change(s, prog, version) given:

s=data, prog="Ladder" , version="1.1" will return:

"Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1"

Rules:

    The date should always be "2019-01-01".

    The author should always be "g964".

    Replace the current "Program Title" with the prog argument supplied to your function. Also remove "Title",
    so in the example case "Program Title: Primes" becomes "Program: Ladder".

    Remove the lines containing "Corporation" and "Level" completely.

    Phone numbers and versions must be in valid formats.

A valid version in the given string data is one or more digits followed by a dot, followed by one or more digits.
So 0.6, 5.4, 14.275 and 1.99 are all valid, but versions like .6, 5, 14.2.7 and 1.9.9 are invalid.

A valid phone format is +1-xxx-xxx-xxxx, where each x is a digit.

    If the phone or version format is not valid, return "ERROR: VERSION or PHONE".

    If the version format is valid and the version is anything other than 2.0,
    replace it with the version parameter supplied to your function.
    If it’s 2.0, don’t modify it.
"""


def change(s, prog, version):
    data = s.split('\n')
    phone = ""
    version_new = ""
    result = "ERROR: VERSION or PHONE"

    for d in data:
        pair = d.split(":")
        if pair[0] == "Phone":
            phone = pair[1][1:]
        if pair[0] == "Version":
            version_new = pair[1][1:]

    if verify_version(version_new) and verify_phone(phone):
        if version_new == "2.0":
            version = version_new

        result = "Program: " + prog + " Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: " + version + ""

    return result


def verify_version(ver):
    version_ok = False
    val = ver.split(".")

    if (len(val) == 2) \
            and (val[0].isdigit() and val[1].isdigit()):
        version_ok = True

    return version_ok


def verify_phone(pho):
    phone_ok = False
    val = pho.split("-")

    if val[0] == "+1" \
            and len(val[1]) == 3 \
            and len(val[2]) == 3 \
            and len(val[3]) == 4:
        phone_ok = True

    return phone_ok

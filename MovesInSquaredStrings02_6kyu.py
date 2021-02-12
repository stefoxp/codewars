def rot(strng):
    result = []

    for s in strng.split("\n"):
        result.append(s[::-1])

    return "\n".join(result[::-1])


def selfie_and_rot(strng):
    result = []
    result = strng.split("\n")
    separator = ""

    for i in range(len(result[0])):
        separator += "."

    return (separator + "\n").join(result) + separator + "\n" + separator + ("\n" + separator).join(rot(strng).split("\n"))


def oper(fct, s):
    return fct(s)

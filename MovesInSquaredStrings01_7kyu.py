def vert_mirror(strng):
    result = []

    for s in strng.split("\n"):
        result.append(s[::-1])

    return "\n".join(result)


def hor_mirror(strng):
    result = []
    s = strng.split("\n")
    length = len(s) + 1

    for i in range(1, length):
        result.append(s[-i])

    return "\n".join(result)


def oper(fct, s):
    return fct(s)

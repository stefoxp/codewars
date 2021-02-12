def order_weight(strng):
    result = []
    values = []

    for d in strng.split():
        weight = 0

        for n in list(d):
            weight += int(n)

        values.append((weight, d))

    values.sort()
    for v in values:
        result.append(v[1])

    return ' '.join(result)

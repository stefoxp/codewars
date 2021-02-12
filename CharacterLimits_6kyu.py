def charCheck(text, mx, spaces):
    print('text:', text, 'mx:', mx)
    limit = False
    result = ''

    if spaces:
        stringa = text
    else:
        stringa = text.replace(' ', '')

    print('stringa:', stringa, 'len(stringa):', len(stringa))

    limit_val = mx - len(stringa)

    if limit_val >= 0:
        limit = True
        limit_val = len(stringa)
    else:
        limit_val = mx

    print('limit_val:', limit_val)

    for i in range(limit_val):
        result += stringa[i]

    return [limit, result]


if __name__ == '__main__':
    charCheck("I am applying for the role of Base Manager on Titan.",
              60,
              True)
    charCheck("I am looking to relocate to the vicinity of Saturn for family reasons.",
              70,
              True)

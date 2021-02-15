def get_pins(observed):
    result = []
    result_map = []
    appoggio = []
    sub_map = [
        ['0', '8'],
        ['1', '2', '4'],
        ['2', '1', '3', '5'],
        ['3', '2', '6'],
        ['4', '1', '5', '7'],
        ['5', '2', '4', '6', '8'],
        ['6', '3', '5', '9'],
        ['7', '4', '8'],
        ['8', '5', '7', '9', '0'],
        ['9', '6', '8']
    ]

    # for s in observed:
    #     for i in range(10):
    #         if i == int(s):

    result_map.append(sub_map[int(observed[0])])

    for i in range(1, len(observed)):
        sub = sub_map[int(observed[i])]

        for r in result_map:
            for v in r:
                for s in sub:
                    # print("v:", v, "s:", s)
                    appoggio.append(v + s)

    # for i in range(len(result_map) - 1):
    #     for r in result_map[i]:
    #         for t in result_map[i + 1]:
    #             result.append(r + t)
        result_map = appoggio

    return result

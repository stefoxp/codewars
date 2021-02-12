def triple_double(num1, num2):
    result = 0
    # interi = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    str01 = str(num1)
    str02 = str(num2)
    tripla_count = 0
    doppia_count = 0

    tripla = False
    doppia = False
    precedente = ""

    for c in str01:
        if c == precedente:
            tripla_count += 1
        else:
            tripla_count = 1

        if tripla_count == 3:
            tripla = True

        precedente = c

    precedente = ""

    for c in str02:
        if c == precedente:
            doppia_count += 1
        else:
            doppia_count = 1

        if doppia_count == 2:
            doppia = True

        precedente = c

    if tripla and doppia:
        result = 1

    return result

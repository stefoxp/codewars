def tops(msg):
    result = ""
    i = 0

    for increment in range(1, len(msg), 4):
        i += increment

        if i < len(msg):
            result = msg[i] + result
        else:
            return result

    return result

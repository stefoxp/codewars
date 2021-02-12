def binary_to_string(binary):
    result = ""
    step = 8

    if binary != "":
        characters = int(len(binary) / step)
        
        # print('char', characters)

        start = 0

        for c in range(characters):
            result += chr(int(binary[start:start + step], 2))
            start += step

    return result

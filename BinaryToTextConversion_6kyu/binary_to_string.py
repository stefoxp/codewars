def binary_to_string(binary):
    result = ""
    step = 8

    if binary != "":
        characters = int(len(binary) / step)
        
        # print('char', characters)

        start = 0

        for c in range(characters):
            result += chr(int(binary[start:start + step], 2))
            #---Above int(string, 2) means treating string as a binary string 
            start += step
            #---Here start is changed to the position of next char

    return result

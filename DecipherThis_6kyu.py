def decipher_this(string):
    result = ""
    words = string.split(" ")

    for w in words:
        if w != "":
            length = len(w)

            for last in range(length, 0, -1):
                # print("-", w[:last], "-")

                if w[:last].isnumeric():

                    # print("-", int(w[:last]), "-")
                    result += chr(int(w[:last]))

                    # print("last:", last)
                    # print("result:", result)

                    break

                if (length - last) > 0:
                    result += w[-1]
                if (length - last) > 2:
                    result += w[last+1:length - 1] + w[last]

            # result += " "

    return result

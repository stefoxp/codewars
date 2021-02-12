def encrypt_this(text):
    result = ""
    words = text.split(" ")

    for w in words:
        if w != "":
            length = len(w)

            if length:
                result += str(ord(w[0]))

                if length > 1:
                    result += w[-1]
                    if length > 2:
                        result += w[2:length - 1] + w[1]

            result += " "

    return result[:-1]

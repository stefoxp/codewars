import string


def play_pass(s, n):
    result = ""
    s_len = len(s)

    for i in range(s_len):
        single_char = s[i]

        if single_char.isdigit():
            result += str(9 - int(single_char))
        elif single_char.isalpha():
            index = string.ascii_uppercase.index(single_char.upper()) + n

            if index >= 26:
                index -= 26

            val = string.ascii_uppercase[index]

            if i % 2 != 0:
                val = val.lower()

            result += val
        else:
            result += single_char

    return result[::-1]

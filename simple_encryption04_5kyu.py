def crypt(encrypt_key, text, encode=True):
    if encrypt_key == 0:
        encrypt_key = "000"

    encrypt_key = list(str(encrypt_key))
    text = list(text)
    result = []

    rows = ("qwertyuiop",
            "asdfghjkl",
            "zxcvbnm,.")
    rows_up = ("QWERTYUIOP",
               "ASDFGHJKL",
               "ZXCVBNM<>")

    for s in text:
        sub = ""

        if not (s in ''.join(rows) + ''.join(rows_up)):
            sub = s
        else:
            for i in range(len(rows)):
                if s in rows[i]:
                    sub = substitute(rows[i], s, encrypt_key[i], encode)
                elif s in rows_up[i]:
                    sub = substitute(rows_up[i], s, encrypt_key[i], encode)

        result.append(sub)
    return ''.join(result)


def substitute(row, s, key, encode=True):
    index = row.index(s)
    if encode:
        index += int(key)
    else:
        index -= int(key)

    if index > (len(row) - 1):
        index = index - len(row)

    sub = row[index]

    return sub


def encrypt(text, encrypt_key):
    return crypt(encrypt_key, text)


def decrypt(text, encrypt_key):
    return crypt(encrypt_key, text, False)

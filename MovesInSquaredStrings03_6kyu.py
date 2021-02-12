def rot_90_clock(strng):
    output_list = transform(strng, True)

    return "\n".join(output_list)


def diag_1_sym(strng):
    output_list = transform(strng)

    return "\n".join(output_list)


def transform(strng, reverse=False):
    input_list = strng.split("\n")
    output_list = []
    for i in range(len(input_list[0])):
        output = ""
        for r in input_list:
            output += r[i]

        if reverse:
            output = output[::-1]

        output_list.append(output)

    return output_list


def selfie_and_diag1(strng):
    output_list = []
    diag_list = transform(strng)

    input_list = strng.split("\n")

    for i in range(len(input_list)):
        output_list.append(input_list[i] + "|" + diag_list[i])

    return "\n".join(output_list)


def oper(fct, s):
    return fct(s)

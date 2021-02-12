import string

vocabulary = string.ascii_uppercase + string.ascii_lowercase + string.digits + ".,:;-?! '()$%&" + '"'


def decrypt(encrypted_text):
    if encrypted_text == "" or encrypted_text is None:
        result = encrypted_text
    else:
        result = step_3(list(encrypted_text))
        result = step_2_dec(list(result))
        result = step_1(list(result))
        result = ''.join(result)

    return result


def encrypt(text):
    if text == "" or text is None:
        result = text
    else:
        result_list = step_1(list(text))
        result_list = step_2(result_list)
        result = step_3(result_list)
        result = ''.join(result)

    return result


def step_1(text_list):
    """
    For every second char do a switch of the case

    :param text_list:
    :return:
    """
    for i in range(len(text_list)):
        if not (text_list[i] in vocabulary):
            raise Exception

        if i % 2 != 0:
            text_list[i] = str.swapcase(text_list[i])

    return text_list


def step_2(step1_list):
    """
    For every char take the index from the region. Take the difference from the region-index of the char before
    (from the input text! Not from the fresh encrypted char before!). (Char2 = Char1-Char2)
    Replace the original char by the char of the difference-value from the region.
    In this step the first letter of the text is unchanged.

    :param step1_list:
    :return:
    """
    result = [step1_list[0]]

    for i in range(1, len(step1_list)):
        index = vocabulary.index(step1_list[i - 1]) - vocabulary.index(step1_list[i])
        result.append(vocabulary[index])

    return result


def step_3(step2_list):
    """
    Replace the first char by the mirror in the given region. ('A' -> '"', 'B' -> '&', ...)

    :param step2_list:
    :return:
    """
    step2_list[0] = vocabulary[len(vocabulary) - (vocabulary.index(step2_list[0]) + 1)]

    return step2_list


def step_2_dec(step3_dec_list):
    """
    REVERSE: For every char take the index from the region. Take the difference from the region-index of the char before
    (from the input text! Not from the fresh encrypted char before!). (Char2 = Char1-Char2)
    Replace the original char by the char of the difference-value from the region.
    In this step the first letter of the text is unchanged.

    :param step3_dec_list:
    :return:
    """
    result = [step3_dec_list[0]]

    for i in range(1, len(step3_dec_list)):
        index = vocabulary.index(result[i - 1]) - vocabulary.index(step3_dec_list[i])
        result.append(vocabulary[index])

    return result

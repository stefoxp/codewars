def first_non_repeating_letter(string):
    result = ""
    vocabulary = []
    stat = []

    for s in string:
        if s.isalpha():
            count = string.count(s.lower()) + string.count(s.upper())
        else:
            count = string.count(s)

        vocabulary.append(s)
        stat.append(count)

        if 1 in stat:
            result = vocabulary[stat.index(1)]

    return result

def smallest(n):
    s = str(n)
    length = len(s)
    result_list = []

    for i in range(length):
        val = s[i]
        s_reduced = s[:i] + s[i + 1:]

        for j in range(length):
            result_list.append([int(s_reduced[:j] + val + s_reduced[j:]), i, j])

    result_list.sort()

    return result_list[0]


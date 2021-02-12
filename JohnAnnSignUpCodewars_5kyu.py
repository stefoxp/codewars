def john(n):
    a, j = set_john_and_ann_katas(n)

    return j


def ann(n):
    a, j = set_john_and_ann_katas(n)

    return a


def sum_john(n):
    a, j = set_john_and_ann_katas(n)

    return sum(j)


def sum_ann(n):
    a, j = set_john_and_ann_katas(n)

    return sum(a)


def set_john_and_ann_katas(n):
    a = [1]
    j = [0]

    for i in range(1, n):
        j_t = j[i - 1]
        j.append(i - a[j_t])

        a_t = a[i - 1]
        a.append(i - j[a_t])

    return a, j

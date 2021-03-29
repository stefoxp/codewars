import string


def rank(st, we, n):
    st = st.split(",")
    length = len(st)
    stwe = []
    ranks = []
    
    if st == [""]:
        result = "No participants"
    elif n > length:
        result = "Not enough participants"
    else:
        for i in range(length):
            stwe.append((st[i], we[i]))

        stwe_ordered = reverse_order(stwe, False)

        for i in range(length):
            ranks.append((calculate(stwe_ordered[i][0], stwe_ordered[i][1]), stwe_ordered[i][0]))

        ranks = reverse_order(ranks)

        result = ranks[n-1][1]
    
    return result


def calculate(first_name, weight):
    length = len(first_name)
    total = length
    
    for i in range(length):
        total += string.ascii_lowercase.index(first_name[i].lower()) + 1

    return total * weight


def reverse_order(original_list, desc=True):
    ordered_list = []

    for i in range(len(original_list)):
        ordered_list.append(original_list[i])

    return sorted(ordered_list, key=lambda x: x[0], reverse=desc)

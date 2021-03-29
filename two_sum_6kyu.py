def two_sum(numbers, target):
    lenght = len(numbers)

    for i in range(lenght):
        for j in range(i + 1, lenght):
            if target == (numbers[i] + numbers[j]):
                return [i, j]

def divisors(n):
    result = 0

    for d in range(1, n + 1):
        if (n % d) == 0:
            result += 1

    return result

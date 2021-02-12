def same_col_seq(val, k, col):
    base = 1
    result = []
    
    if col == 'yellow':
        base += 1
    elif col == 'blue':
        base += 2
        
    for c in range(val + 1, val * k * 3):
        print(c)
    
    return result


def recur(n):
    """
    f(1) = 1
    f(n) = f(n - 1) + n
    """
    if n == 1:
        return 1
    else:
        return n + recur(n - 1)


if __name__ == '__main__':
    print('recur(1):', recur(1))
    print('recur(2):', recur(2))
    print('recur(3):', recur(3))
    print('recur(4):', recur(4))
    print('recur(5):', recur(5))
    print('recur(100):', recur(100))

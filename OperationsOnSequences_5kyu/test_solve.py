from solve import solve


def check(res, exp):
    if len(res) != 2:
        return False
    if res[0] < 0 or res[1] < 0 or type(res[0]) != int or type(res[1]) != int:
        print("A and B should be nonnegative integers")
        return False
    p = exp[0] ** 2 + exp[1] ** 2
    pp = res[0] ** 2 + res[1] ** 2
    if p != pp:
        print("Incorrect sum of squares")
        return False
    return True


def ting(arr, exp):
    ans = solve(arr)
    bl = check(ans, exp)
    assert bl is True


def test_basic():
    a0 = [0, 7, 0, 0]
    ting(a0, [0, 0])


'''
        a1 = [1, 3, 1, 2, 1, 5, 1, 9]
        testing(a1, [250, 210])
        a2 = [2, 1, 3, 4]
        testing(a2, [2, 11])
        a3 = [3, 9, 8, 4, 6, 8, 7, 8, 4, 8, 5, 6, 6, 4, 4, 5]
        testing(a3, [13243200, 25905600])
'''

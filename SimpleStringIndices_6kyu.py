"""
In this Kata, you will be given a string with brackets and an index of an opening bracket and your task will be to return the index of the matching closing bracket. Both the input and returned index are 0-based except in Fortran where it is 1-based. An opening brace will always have a closing brace. Return -1 if there is no answer (in Haskell, return Nothing; in Fortran, return 0; in Go, return an error)
Examples

solve("((1)23(45))(aB)", 0) = 10 -- the opening brace at index 0 matches the closing brace at index 10
solve("((1)23(45))(aB)", 1) = 3 
solve("((1)23(45))(aB)", 2) = -1 -- there is no opening bracket at index 2, so return -1
solve("((1)23(45))(aB)", 6) = 9
solve("((1)23(45))(aB)", 11) = 14
solve("((>)|?(*'))(yZ)", 11) = 14

Input will consist of letters, numbers and special characters, but no spaces. The only brackets will be ( and ). 
"""


# print("st (originale) =", st)

# print("last_open =", last_open)
# print("first_close =", first_close)

# print("st =", st)


def solve(st, idx):
    last_open = len(st) - 1

    for i in range(len(st) - 1):
        last_open = st.rfind("(", 0, last_open)
        first_close = st.find(")", last_open, len(st))

        if first_close != -1:
            # substitution
            st = st[0:first_close] + "-" + st[first_close + 1:]

        if idx == last_open:
            return first_close

    return -1


if __name__ == '__main__':
    risultato = solve("((1)23(45))(aB)", 0)
    test = 10 == risultato
    print("solve('((1)23(45))(aB)', 0) = 10 ?",
          test, " risultato =", risultato)
    risultato = solve("((1)23(45))(aB)", 1)
    test = 3 == risultato
    print("solve('((1)23(45))(aB)', 1) = 3 ?",
          test, " risultato =", risultato)
    risultato = solve("((1)23(45))(aB)", 2)
    test = -1 == risultato
    print("solve('((1)23(45))(aB)', 2) = −1 ?",
          test, " risultato =", risultato)
    risultato = solve("((1)23(45))(aB)", 6)
    test = 9 == risultato
    print("solve('((1)23(45))(aB)', 6) = 9 ?",
          test, " risultato =", risultato)

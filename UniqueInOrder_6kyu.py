def unique_in_order(iterable):
    risultato = []
    
    for i in range(len(iterable)):
        if i == 0:
            risultato = [iterable[0]]
        elif iterable[i] != iterable[i-1]:
            risultato.append(iterable[i])
            
    return risultato


if __name__ == '__main__':
    print("unique_in_order('A')", unique_in_order('A'))
    print("unique_in_order('AABBBCDDD')", unique_in_order('AABBBCDDD'))

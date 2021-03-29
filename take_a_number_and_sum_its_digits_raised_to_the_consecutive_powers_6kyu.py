import math

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    risultato = []
    for number in range(a, b + 1):
        partial = 0
        power = 1
        number_to_str = str(number)
        for c in range(len(number_to_str)):
            partial += math.pow(int(number_to_str[c]), power)
            power += 1
            
        if number == partial:
            risultato.append(number)
            
    return risultato

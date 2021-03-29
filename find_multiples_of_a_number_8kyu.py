def find_multiples(integer, limit):
    multiplo = integer
    lista = [integer]
    
    while multiplo <= (limit - integer):
        multiplo += integer
        lista.append(multiplo)

    return lista

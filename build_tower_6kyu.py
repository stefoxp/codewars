def tower_builder(n_floors):
    element = '*'
    lista = [element]
    risultato = []
    step = 1
    
    # while step < n_floors:
    for c in range(1, n_floors):
        step += 2
        lista.append(element * step)
        
    for riga in lista:
        spaces = int((step - len(riga)) / 2)
        print('riga:', riga, 'spazi:', spaces)
        risultato.append(' ' * spaces + riga + ' ' * spaces)
    
    return risultato


if __name__ == '__main__':
    print('tower_builder(1):', tower_builder(1))
    print('tower_builder(2):', tower_builder(2))
    print('tower_builder(3):', tower_builder(3))
    print('tower_builder(4):', tower_builder(4))
    print('tower_builder(6):', tower_builder(6))

def rps(p1, p2):
    codice = -1
    risultato = ''
    punti = ((('scissors', 'scissors'), 0),
            (('paper', 'paper'), 0),
            (('rock', 'rock'), 0),
            (('scissors', 'paper'), 1),
            (('paper', 'rock'), 1),
            (('rock', 'scissors'), 1),
            (('paper', 'scissors'), 2),
            (('rock', 'paper'), 2),
            (('scissors', 'rock'), 2))
    
    for punteggio in punti:
        if (p1, p2) == punteggio[0]:
            codice = punteggio[1]
            
    if codice == 0:
        risultato = 'Draw!'
    elif codice == 1:
        risultato = "Player 1 won!"
    else:
        risultato = "Player 2 won!"
        
    return risultato

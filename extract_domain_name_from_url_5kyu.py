def domain_name(url):
    risultato = ''
    
    inizio = url.find('//')
    www = url.find('www.')
    if www != -1:
        inizio = inizio + 3
        fine = url.find('.', www + 4)
    else:
        fine = url.find('.', inizio + 2)
    
    risultato = url[inizio + 2: fine]
    
    return risultato

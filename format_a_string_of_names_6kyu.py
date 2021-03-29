def namelist(names):
    result = ''
    lunghezza = len(names)
    
    if lunghezza > 1:
        result += names[0]['name']
        
        for value in names[1:lunghezza-1]:
            result += ', ' + value['name']
            
        result += ' & ' + names[lunghezza - 1]['name']
    elif lunghezza == 1:
        result += names[0]['name']
        
    return result

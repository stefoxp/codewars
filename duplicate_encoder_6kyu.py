def duplicate_encode(word):
    word_list = []
    duplicati = []
    list = []
    
    for c in range(len(word)):
        carattere = word[c].lower()
        
        if carattere not in word_list:
            word_list.append(carattere)
        else:
            duplicati.append(carattere)

    for c in range(len(word)):
        carattere = word[c].lower()
        if carattere in duplicati:
            list.append(')')
        else:
            list.append('(')
    
    return ''.join(list)

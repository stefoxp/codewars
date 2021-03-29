import string

def is_pangram(s):
    result = True
    caratteri = []
    
    for c in s:
        if c in string.ascii_letters:
            caratteri.append(c.lower())
            
    for c in string.ascii_lowercase:
        if c not in caratteri:
            result = False
    
    return result

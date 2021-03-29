import string

def decrypt(code):
    text = ''
    words = []
    numbers = []
    results = []
    
    words = code.split(' ')
    
    for w in range(len(words)):
        numbers.append(0)
        
        for c in words[w]:
            if c in string.digits:
                numbers[w] += int(c)
    
    for n in numbers:
        if n > 26:
            results.append(n - 27)
        else:
            results.append(n)
    
    for n in results:
        if n == 0:
            text += ' '
        else:
            text += string.ascii_lowercase[n - 1]
        
    return text

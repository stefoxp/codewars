import string

def duplicate_count(text):
    result = 0
    count = []
    alphabet = string.ascii_letters + string.digits
    for i in range(len(alphabet)):
        count.append(0)
    
    for c in text:
        index = alphabet.find(c.lower())
        count[index] += 1
        
    for e in count:
        if e > 1:
            result += 1
    print(text)
    
    return result

def delete_digit(n):
    n = str(n)
    l = []
    max = 0
    
    for i in range(len(n)):
        l.append(int(n[:i] + n[i + 1:]))
        
    for value in l:
        if value > max:
            max = value
    
    return max

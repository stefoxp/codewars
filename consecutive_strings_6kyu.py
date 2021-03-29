def longest_consec(strarr, k):
    result = ""
    n = len(strarr)
    if n != 0 and k <= n and k >= 0:
        length = 0
        index = 0
        partial = ''
        
        for s in strarr:
            index = strarr.index(s)
            if index <= (n - k):
                partial = ''.join(strarr[index : index + k])
            else:
                partial = strarr[index]
            
            l = len(partial)
            
            if l > length:
                length = l
                result = partial
      
    return result

def in_array(array1, array2):
    result = []
    
    for st in array1:
        for st2 in array2:
            if st in st2:
                result.append(st)
        
    result = set(result)
    
    result = sorted(list(result))
    
    return result

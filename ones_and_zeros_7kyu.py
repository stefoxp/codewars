def binary_array_to_number(arr):
    s = ''
    
    for element in arr:
        s += str(element)
    
    return int(s, 2)

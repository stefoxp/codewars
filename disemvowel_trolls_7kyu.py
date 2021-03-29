def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    result = []
    
    for letter in string:
        if not(letter in vowels):
            result.append(letter)
    
    return ''.join(result)

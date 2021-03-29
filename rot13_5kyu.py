import string
from codecs import encode as _dont_use_this_

def rot13(message):
    result = ''
    alphabet_low = string.ascii_lowercase
    alphabet_upp = string.ascii_uppercase
    
    for c in message:
        if c in alphabet_low:
            index = alphabet_low.find(c) + 13
            if index < len(alphabet_low):
                result += alphabet_low[index]
            else:
                result += alphabet_low[index - len(alphabet_low)]
        elif c in alphabet_upp:
            index = alphabet_upp.find(c) + 13
            if index < len(alphabet_upp):
                result += alphabet_upp[index]
            else:
                result += alphabet_upp[index - len(alphabet_upp)]
        else:
            result += c
    
    return result

# dict preloaded

"""
def decode(string):
    if string == "":
        return string
    
    words = string.split('  ')
  
    string = ''
  
    for w in words:
        letters = w.split(' ')
    
        for l in letters:
            string += dict[l]
            
        string += ' '
      
    return string[:len(string)-1]
"""


def decode(string):
    if string == "":
        return string
    
    alphabet = {'.-': 'a', 
                '-...': 'b',
                '-.-.': 'c',
                '-..': 'd',
                '.': 'e',
                '..-.': 'f',
                '--.': 'g',
                '....': 'h',
                '..': 'i',
                '.---': 'j',
                '-.-': 'k',
                '.-..': 'L',
                '--': 'm',
                '-.': 'n',
                '---': 'o',
                '.--.': 'p',
                '--.-': 'q',
                '.-.': 'r',
                '...': 's',
                '-': 't',
                '..-': 'u',
                '...-': 'v',
                '.--': 'w',
                '-..-': 'x',
                '-.--': 'y',
                '--..': 'z',
                '.----': '1',
                '..---': '2',
                '...--': '3',
                '....-': '4',
                '.....': '5',
                '-....': '6',
                '--...': '7',
                '---..': '8',
                '----.': '9',
                '-----': '0'}
    
    words = string.split('  ')
  
    string = ''
  
    for w in words:
        letters = w.split(' ')
    
        for L in letters:
            string += alphabet[L]
            
        string += ' '
      
    return string[:len(string)-1]
  

if __name__ == '__main__':
    atteso = "hello world"
    risultato = decode(".... . .-.. .-.. ---  .-- --- .-. .-.. -..")
    print(atteso,
          risultato,
          atteso == risultato)

    atteso = "1st and 2nd"
    risultato = decode(".---- ... -  .- -. -..  ..--- -. -..")
    print(atteso,
          risultato,
          atteso == risultato)

    atteso = "i am a test"
    risultato = decode("..  .- --  .-  - . ... -")
    print(atteso,
          risultato,
          atteso == risultato)

    atteso = "abcdefghijklmnopqrstuvwxyz0123456789"
    risultato = decode(".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.")
    print(atteso,
          risultato,
          atteso == risultato)

    atteso = ""
    risultato = decode("")
    print(atteso,
          risultato,
          atteso == risultato)


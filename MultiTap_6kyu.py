def presses(phrase):
    keys = 0
    '''
    one = ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w']
    two = ['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x']
    three = ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y']
    '''
    keymap = ['1', 'abc2', 'def3',
              'ghi4', 'jkl5', 'mno6',
              'pqrs7', 'tuv8', 'wxyz9',
              '*', ' 0', '#']
    
    for c in phrase:
        tap = 0
        # print('c:', c.lower())
        for k in keymap:
            if c.lower() in k:
                tap = k.find(c.lower()) + 1
        keys += tap

        # debug
        # print('c:', c.lower(), 'tap:', tap, 'keys:', keys)
        
    return keys


if __name__ == '__main__':
    print('presses("WHERE DO U WANT 2 MEET L8R"):',
          presses("WHERE DO U WANT 2 MEET L8R"))

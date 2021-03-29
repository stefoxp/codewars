import string

def stock_list(listOfArt, listOfCat):
    count = dict([('', 0)])
    result = ''
    
    if ((len(listOfArt) != 0) and (len(listOfCat) != 0)):
        for b in listOfCat:
            count[b[0]] = 0
            
        for b in listOfArt:
            if b[0] in count:
                count[b[0]] += int(b[b.find(' '):])
    
        for key in listOfCat:
            if result != '':
                result += ' - '
            result += '(' + key + ' : ' + str(count[key]) + ')'
    
    return result

def likes(names):
    msg = 'no one likes this'
    people = len(names)
    
    # msg_lst = (0, 'no one likes this')
    
    if people == 1:
        msg = names[0] + ' likes this'
    elif people == 2:
        msg = names[0] + ' and ' + names[1] + ' like this'
    elif people == 3:
        msg = names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    elif people > 3:
        msg = names[0] + ', ' + names[1] + ' and ' + str(people - 2) + ' others like this'
    
    return msg

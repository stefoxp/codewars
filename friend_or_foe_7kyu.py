def friend(x):
    friends = []
    
    for element in x:
        if len(element) == 4:
            friends.append(element)
            
    return friends

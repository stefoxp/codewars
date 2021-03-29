def show_sequence(n):
    result = str(n) + "<0"
    sum = 0
    
    if n == 0:
        result = "0=0"
    elif(n > 0):
        result = ""
        for i in range(0, n+1):
            sum += i
            result += "+" + str(i)
            
        result = result[1:] + " = " + str(sum)
    
    return result

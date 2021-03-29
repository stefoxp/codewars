def weather_info (temp):
    c = convertToCelsius(temp)
    if (c > 0):
        return (str(c) + " is above freezing temperature")
    else:
        return (str(c) + " is freezing temperature")
    
def convertToCelsius (temperature):
    celsius = (temperature - 32) * 5.0 / 9
    return celsius

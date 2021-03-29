"""
Determine whether a positive integer number is colorful or not.

263 is a colorful number because [2, 6, 3, 2*6, 6*3, 2*6*3] are all different; whereas 236 is not colorful, because [2, 3, 6, 2*3, 3*6, 2*3*6] have 6 twice.

So take all consecutive subsets of digits, take their product and ensure all the products are different.
Examples

263  -->  true
236  -->  false
"""


def colorful(number):
    verified = False
    numbers = []
    count = 0
    
    for n in str(number):
        numbers.append(int(n))
    
    products = numbers.copy()
    
    for i in range(len(numbers) - 1):
        products.append(numbers[i] * numbers[i + 1])
    
    for p in products:
        count += products.count(p)
        
    if count == len(products):
        verified = True

    return verified

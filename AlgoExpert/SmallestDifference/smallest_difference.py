import math

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.

    arrayOne.sort()
    arrayTwo.sort()
    
    max = math.inf
    pair = []

    i = 0 
    j = 0

    while i < len(arrayOne) and j < len(arrayTwo):
        if arrayOne[i] == arrayTwo[j]:
            return [arrayOne[i], arrayTwo[j]]

        difference = abs(arrayOne[i] - arrayTwo[j])

        if difference < max:
            pair = [arrayOne[i], arrayTwo[j]]
            max = difference

        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1
        
        


        
                
    return pair

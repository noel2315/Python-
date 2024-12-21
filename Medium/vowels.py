import math

def countVowelStrings(n):
    return math.comb(n + 4, 4)

n = 3
print(countVowelStrings(n)) 

import math

def absval(val, root = 0):
    if val >= root:
        return val - root
    else:
        return root - val

def linear(val, low, high):
    val = val - low
    high = high - low
    return val / high

def is_prime(s):
    if s == 2:
        return True
    if s % 2 == 0:
        return False
    for f1 in range(3, s, 2):
        for f2 in range(3, s):
            if f1 * f2 == s:
                return False
    return True

def max(numbs):
    max = None
    for i in numbs:
        if max == None:
            max = i
        elif i > max:
            max = i
    return max

def min(numbs):
    min = None
    for i in numbs:
        if min == None:
            min = i
        elif i < min:
            min = i
    return min

def mean(numbs, int = False):
    sum = 0
    for i in numbs:
        sum += i
    if int == False:
        return sum / len(numbs)
    if int == True:
        return sum // len(numbs)
    
def mode(numbs):
    dict = {}
    for i in numbs:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1

    values = []
    number = []
    for key in dict:
       values.append(dict[key])
       number.append(key)
    
    max = None
    ind = 0
    maxi = 0
    for i in values:
        if max == None:
            max = i
            maxi = ind
        elif i > max:
            max = i
            maxi = ind
        ind += 1
    return number[maxi]

def listRange(numbs):
    
    max = None
    for i in numbs:
        if max == None:
            max = i
        elif i > max:
            max = i
    
    
    min = None
    for i in numbs:
        if min == None:
            min = i
        elif i < min:
            min = i

    return max - min

def fact(n):
    if n == 0:
        return 1
    sum = 1
    for i in range(1,n + 1):
        print(i)
        sum *= i
    return sum


def add(*vectors): #vector addition, not addition though in theory that should still work if entered as a list/array
    max = None
    for vector in vectors:
        if max == None:
            max = len(vector)
        elif len(vector) >= max:
            max = len(vector)
    final = []
    for i in range(max):
        final.append(0)
    for vector in vectors:
        ind = 0
        for n in vector:
            final[ind] = final[ind] + n
            ind += 1
    return final

def qudratic(a,b,c):
    d = b*b - 4*a*c
    if d < 0:
        return None
    return [(-b + math.sqrt(d)) / 2*a,(-b - math.sqrt(d)) / 2*a]

def prime(n): # a simpler and probably faster solution to primes as opposed to the solution I made on 15-24
    for i in range(n):
        if n % i == 0:
            if i != 0 and i != n:
                return False
    return True

#!/usr/bin/python

import sys
import time
import math
import itertools
    
def Eratostheses(n):
    numberList = range(2, n +1) 
    primeList = []
    #after sqrt(n) every multiplication is on the other side i.e. 10*90 -> 90*10, so there are only primes left
    maxCalc = math.sqrt(n) 
    while len(numberList) > 0 and numberList[0]< maxCalc:
         # the first number is always a prime
        prime = numberList[0]
        primeList.append(prime)
        #remove all items divisible by prime 
        numberList= [i for i in numberList if (i%prime !=0)] 
    #all primes below root(n) + above root(n)
    return primeList+numberList 
    
def Sundaram(n):
    highestNr = int((n-1)*0.5 + 1) # because you multiply everything by 2 and add 1, you need only go to (n-1)/2 to get all primes below n
    numberList = range(1, highestNr) 
    #calculate all numbers that should be removed
    removeList = [(i + j + 2*i*j) for i, j in itertools.product(range(1, highestNr), range(1, highestNr)) if (i + j + 2*i*j) < highestNr]
    numberList= [2*y+1 for y in numberList if (y not in removeList)]
    return [2] + numberList
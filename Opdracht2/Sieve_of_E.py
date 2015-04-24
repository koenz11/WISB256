#!/usr/bin/python

import sys
import time
import math
    
def SieveE(tot):
    numberList = range(2, tot +1) 
    primeList = []
    maxCalc = math.sqrt(tot)
    while len(numberList) > 0 and numberList[0]< maxCalc: 
        prime = numberList[0]
        primeList.append(prime)
        numberList= [x for x in numberList if x%prime !=0] #remove all items divisible by prime 
    return primeList+numberList #all primes below root(n) + above root(n)

#//////////arguments
arguments = sys.argv

highestNr = int(sys.argv[1])
fileName = sys.argv[2]
#/////////

T1 = time.perf_counter()


primeList = SieveE(highestNr)

T2 = time.perf_counter()

file = open(fileName, 'w')
for prime in primeList:
    file.write(str(prime) + '\n')

print('Found', len(primeList), 'Prime numbers smaller than', highestNr, 'in', T2 - T1, 'sec.')
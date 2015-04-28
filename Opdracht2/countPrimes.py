import sys
import math
#//////////arguments
arguments = sys.argv

fileName = sys.argv[1]
#/////////

file = open(fileName, 'r')

lastPrime = 0
primeCount = 0
twinCount = 0
#count all the primes
for line in file:
    prime = int(line)
    primeCount+= 1
    #check if this prime is twin with the last prime
    if lastPrime + 2 == prime:
        twinCount += 1
    lastPrime = prime
    
#calculate the elements needed for the formula
lastLog = math.log(lastPrime)
constant = 0.6601618
primeFormula = lastPrime / lastLog
twinFormula = 2* constant* lastPrime / (lastLog*lastLog)

print('Largest Prime =', lastPrime)
print('--------------------------------')
print('pi(N)         =', primeCount)
print('N/Log(N)      =', primeFormula)
print('ratio         =', primeCount/primeFormula)
print('--------------------------------')
print('pi_2(N)       =', twinCount)
print('2CN/Log(N)^2  =', twinFormula)
print('ratio         =', twinCount/twinFormula)
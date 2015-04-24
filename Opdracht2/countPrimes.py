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
for line in file:
    prime = int(line)
    primeCount+= 1
    if lastPrime + 2 == prime:
        twinCount += 1
    lastPrime = prime
##########################################################################
total = 1000000
#########################################################################
totalLog = math.log(total)
constant = 0.6601618
primeFormulaPart = total / totalLog
primeFormula = primeFormulaPart/primeCount  
twinFormulaPart = 2* constant* total / (totalLog*totalLog)
twinFormula = twinFormulaPart/twinCount

print 'Largest Prime =', lastPrime 
print '--------------------------------'
print 'pi(N)         =', primeCount
print 'N/Log(N)      =', primeFormulaPart
print 'ratio         =', primeFormula
print '--------------------------------'
print 'pi_2(N)       =', twinCount
print '2CN/Log(N)^2  =', twinFormulaPart
print 'ratio         =', twinFormula
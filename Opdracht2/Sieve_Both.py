#!/usr/bin/python

import sys
import time
import Sieve

#//////////arguments
arguments = sys.argv

highestNr = int(sys.argv[1])
fileName = sys.argv[2]
fileName2 = sys.argv[3]
#/////////

T1 = time.perf_counter()
primeList = Sieve.Eratostheses(highestNr)
T2 = time.perf_counter()

'''
you'll see that the algorithm found by Sundaram is slower then the one found by Eratostheses.
'''

T3 = time.perf_counter()
primeList2 = Sieve.Sundaram(highestNr)
T4 = time.perf_counter()


file = open(fileName, 'w')
for prime in primeList:
    file.write(str(prime) + '\n')

file2 = open("prime2.dat", 'w')
for prime in primeList2:
    file2.write(str(prime) + '\n')

print('SieveEratostheses Found', len(primeList), 'Prime numbers smaller than', highestNr, 'in', T2 - T1, 'sec.')
print('--------------------------------------------')
print('SieveSundaram Found', len(primeList2), 'Prime numbers smaller than', highestNr, 'in', T4 - T3, 'sec.')
print('--------------------------------------------')

#!/usr/bin/python

import sys
import time
import Sieve
arguments = sys.argv

highestNr = int(sys.argv[1])
fileName = sys.argv[2]
#/////////

T1 = time.perf_counter()
primeList = Sieve.Sundaram(highestNr)
T2 = time.perf_counter()

file = open(fileName, 'w')
for prime in primeList:
    file.write(str(prime) + '\n')

print('Found', len(primeList), 'Prime numbers smaller than', highestNr, 'in', T2 - T1, 'sec.')
print('--------------------------------------------')
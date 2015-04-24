#!/usr/bin/python
import math

savedPrimes = [2]
maxPrime = 2

def nextPrime(lastPrime):
    global maxPrime
    global savedPrimes
    nextNumber = lastPrime
    prime = False
   
    while not prime:
        nextNumber += 1
        prime = True
        
        if nextNumber <= maxPrime:
            if nextNumber in savedPrimes:
                return nextNumber
        
        
        for i in savedPrimes:
            div = nextNumber % i == 0
            prime = prime and not div
            if not prime:
                break
    'print(savedPrimes)'
    savedPrimes.append(nextNumber)   
    maxPrime = max(maxPrime, nextNumber)
    return nextNumber

def numDivisors(nr):
    factors = primefactors(nr)
    divisors = 1;
    for key, value in factors.items():
        if not value == 0:
            divisors *=  (value+1)
    return divisors
    

def primefactors(nr):
    Dict = {}
    remaining = nr
    prime = 2
    while prime <= remaining:
        grade = 0
        while (remaining % prime == 0):
            remaining /= prime
            grade += 1
        Dict[prime] = grade
        prime = nextPrime(prime)
        'print(str(prime) + " - " + str(remaining))'
        
    'print(str(nr) + " - " + str(Dict))'
    return Dict



def primeNumbers(tot):
    SieveE(tot)
    
    
def SieveE(tot):
    numberList = range(2, tot +1) 
    primeList = []
    maxCalc = math.sqrt(tot)
    while len(numberList) > 0 and numberList[0]< maxCalc: 
        prime = numberList[0]
        primeList.append(prime)
        numberList= [x for x in numberList if x%prime !=0] #remove all items divisible by prime 
    return primeList+numberList #all primes below root(n) + above root(n)
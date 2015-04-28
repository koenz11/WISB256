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
    global maxPrime
    global savedPrimes
    if maxPrime < nr:
        savedPrimes = primeNumbers(nr)
        maxPrime = max(savedPrimes)
    
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
    return SieveEratostheses(tot)
    
    
def SieveEratostheses(n):
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
    
def SieveSundaram(n):
    highestNr = int((n-1)*0.5) # because you multiply everything by 2 and add 1, you need only go to (n-1)/2 to get all primes below n
    numberList = range(1, highestNr) 
    #calculate all numbers that should be removed
    removeList = [(i + j + 2*i*j) for i, j in itertools.product(range(1, highestNr), range(1, highestNr)) if (i + j + 2*i*j) < highestNr]
    numberList= [2*y+1 for y in numberList if (y not in removeList)]
    return [2] + numberList
    
    
    
    
    
    
    
from timing import timing_function
from arithmetic import primes, isPrime
from typing import List

primes = primes(1000)     
while primes[0] <= 40:
    primes.pop(0)

def quadratic(a, b, n):
    return n**2+a*n+b

def consecutive(a, b):
    n = 0
    while isPrime(quadratic(a, b, n)):
        n +=1
    return n

def euler_27():
    maxConsecutive = -1
    for a in range(0, 1000):
        for b in primes:
            aux = consecutive(a, b)
            if aux > maxConsecutive:
                maxA, maxB, maxConsecutive = a, b, aux
            aux = consecutive(-a, b)
            if aux > maxConsecutive:
                maxA, maxB, maxConsecutive = -a, b, aux
            aux = consecutive(a, -b)
            if aux > maxConsecutive:
                maxA, MaxB, maxConsecutive = a, -b, aux
            aux = consecutive(-a, -b)           
            if aux > maxConsecutive:
                maxA, MaxB, maxConsecutive = -a, -b, aux
    return (maxA, maxB, maxA * maxB, maxConsecutive)

def euler_27_b():
    maxConsecutive = -1
    for a in range(0, 1000):
        for b in primes:
#           aux = consecutive(a, b)
            if consecutive(a, b) > maxConsecutive:
                maxA, maxB, maxConsecutive = a, b, consecutive(a, b)
#            aux = consecutive(-a, b)
            if consecutive(-a, b) > maxConsecutive:
                maxA, maxB, maxConsecutive = -a, b, consecutive(-a, b)
#            aux = consecutive(a, -b)
            if consecutive(a, -b) > maxConsecutive:
                maxA, MaxB, maxConsecutive = a, -b,consecutive(a, -b) 
#            aux = consecutive(-a, -b)           
            if consecutive(-a,-b) > maxConsecutive:
                maxA, MaxB, maxConsecutive = -a, -b, consecutive(-a, -b)    
    return (maxA, maxB, maxA * maxB, maxConsecutive)    

def main():
    print(timing_function(euler_27))

main()


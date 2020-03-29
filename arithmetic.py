#!/usr/bin/env python3

import time
import math
import functools
import operator
from typing import List

def timing_function(some_function, arg = 1000):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        print(some_function(arg))
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + " seconds"
    return wrapper()


def sumOfPowerDigits(n, p: "The power is 1 by default" = 1):
    """Returns the sum of the p-powers of the digits of n"""  
    if n < 0:   return None ## Check n >= 0
    accum = 0 
    while n >= 10:
        r = n % 10
        accum += r**p
        n = (n - r) // 10
    return accum + n**p

def digits(n):
    """Returns the list of digits of n"""  
    if n < 0: return [] ## Check n >= 0
    ds = [] 
    while n >= 10:
        r = n % 10
        ds.insert(0,r)
        n = (n - r) // 10
    ds.insert(0, n)
    return ds

## Combinatorics

def factorial(n):
    return functools.reduce(operator.mul, range(1, n + 1), 1)

def permutations(n, k):
    return functools.reduce(operator.mul, range(n, n-k, -1), 1)

def binomial(n, k):
    if k > n or k < 0:
        return 0
    if n == 0 or n == k:
        return 1
    return permutations(n, k) // factorial(k)

## Combinatorics

def alpha(n: int, p :int) -> int:
    """
    Returns the largest nonnegative power of prime p that divides n.
    For example alpha(100, 2) = 2, aplha(100, 3) = 0, alpha(125, 5) = 3.  
    """
    assert (n > 1 and p > 1), "Not a valid input"
    count = 0
    while (n % p == 0):
        count += 1
        n /= p
    return count

def q(n: int) -> int:
    """
    Returns the smallest divisor of n bigger than 1.
    For example q(100) = 2, q(15) = 3, q(125) = 5.  
    """
    assert (n > 1), "Not a valid input n = {} must be > 1".format(n)
    ub = math.ceil(math.sqrt(n))
    if n % 2 == 0: return 2
    d = n    
    for i in range(3, ub + 1, 2):
        if n % i == 0:
            d = i
            break
    return d

def prime_factorization(n: int) -> List[int]:
    """
    Returns the prime factorization of n.
    For example prime_factorization(100) = [(2, 2), (5, 2)]
    """
    ls = []
    while (n > 1):
        p = q(n)
        a = alpha(n, p)
        ls.append((p, a))
        n = n // p**a
    return ls

def divisors(n: int) -> List[int]:
    """Returns the list of divisors of a positive integer.
     Example: >>>divisors(10): [1, 2, 5, 10]"""
    ls = []
    d = math.ceil(math.sqrt(n))
    ls = [i for i in range(1, d) if n % i == 0]
    rs = [n // i for i in ls]
    if d**2 == n and n % d == 0:
        ls.append(d)
    return ls + rs[::-1]

def isPrime(n):
    """Return True if n is prime, False otherwise"""
    n = abs(n)
    if n == 0:
        return False
    if n == 1:      return False
    if n in [2, 3, 5]: return True
    return n == q(n)

#Sequences
def fibonacci(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        a, b = b, a + b
        count += 1
    return a

def triangular(n):
    a = 0
    count = 1
    while count <= n:
        a = a + count
        count += 1
    return a

## Create a table of primes
def table_of_primes(fname: "file name" = "primes.txt",
                    prop: "stop when proposition is false" = lambda n: n <= 1000):
    """
Some useful facts:
. All prime except 2 are odd
. All primes greater than 3 can be written are 1 or 5 mod 6
. If anumber has a proper divisor greater than 1,
  it has a proper divisor less or equal than sqrt(n).  
    """
    with open(fname, 'w') as f:
        f.write(str(2) + "\n")
        f.write(str(3) + "\n")
        n = 5
        while prop(n):
            if isPrime(n):
                f.write(str(n) + "\n")               
            n += 2
            if isPrime(n):
                f.write(str(n) + "\n")
            n += 4 
    
## Create a List of primes
def primes(n : int) -> List[int]:    
    """ Returns the list of primes less or equal than n"""
    ls = list()
    if n <= 1:
        return ls
    ls.append(2)
    if n <= 2:
        return ls
    ls.append(3)
    if n <= 3:
        return ls
    p = 5
    while p <= n:
        if isPrime(p):
            ls.append(p)
        if p + 2 > n:
            return ls
        p += 2
        if isPrime(p):
            ls.append(p)
        p += 4
    return ls

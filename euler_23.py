from timing import timing_function
from arithmetic import divisors, triangular
from typing import List

def sumOfProperDivisors(a : int) -> int:
    return sum(divisors(a)) - a

def isAbundant(a : int) -> bool:
    b = sumOfProperDivisors(a)
    return b > a
            
def abundants(n : int) -> List[int]:
    ls = list()
    for i in range(12, n):
        if isAbundant(i):
            ls.append(i)
    return ls

abds = abundants(28123)

def isSumOfAbundant(n : int) -> bool:
    for a in abds:
        if a >= n:
            return False
        elif isAbundant(n - a):
            return True
        else:
            continue
    
def euler_23():
    accum = sum(range(1, 24))
    for n in range(25, 28123):
        if not isSumOfAbundant(n):
            accum += n
    return accum

def main():
    print(timing_function(euler_23))

#main()

## user: norvig
aSet = set(i for i in range(1,28124) if isAbundant(i))

def abundantsum(i):
    return any(i-a in aSet for a in aSet)

def abundantSum(i):
    return any(i-a in abds for a in abds)

def euler_any():
    return sum(i for i in range(1,28124) if not abundantsum(i))
def main_1():
    print(timing_function(euler_any))

main_1()    
#####################################
def member(n : int, ls : List[int]):
    """Returns True if n is in ls.
    The list ls is an ordered list"""
    if ls == []:
        return False
    if n > ls[len(ls)-1]:
        return False
    for a in ls:
        if a > n:
            return False
        if a == n:
            return True
    return False

def findPair(n : int, ls : List[int]) -> bool:
    """
    Returns True if there is a pair in the list with given sum n
    Assume ls is an ordered list of positive integers
    """
    for a in ls:
        if a >= n:
            return False
        if member(n - a, ls):
            return True
    return False

def euler_23_find():
    ls = abundants(28123)
    accum = sum(range(1, 24))
    for n in range(25, 28123):
        if not findPair(n, ls):
            accum += n
    return accum

def euler_23_bad():
    ls = abundants(28123)
    rs = list()
    for i in ls:
        for j in ls:
            rs.append(i+j)
    accum = sum(range(1, 24))
    for n in range(25, 28123):
        if not member(n, rs):
            accum += n
    return accum

def sumOfAbundant(n : int) -> bool:
    for a in range(1, n):
        if isAbundant(a) and isAbundant(n - a):
            return True
        if a > n - a:
            return False

def member(n : int):
    """Returns True if n is in ls.
    The list ls is an ordered list"""
    i = 0
    m = len(abds)
    while i < m:
        if n < abds[i]:
            return False
        elif n == abds[i]:
                return True
        else:
            i +=1
    return False

def abundant(fname):
    with open(fname, 'w') as f:
        for i in range(1, 28123):
            if isAbundant(i):
                f.write(str(i)+"\n")

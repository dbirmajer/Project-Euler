from timing import timing_function
from arithmetic import divisors, triangular
from typing import List

def sumOfProperDivisors(a : int) -> int:
    return sum(divisors(a)) - a

def isAmicable(a : int) -> bool:
    b = sumOfProperDivisors(a)
    if b == a:
        return False
    elif a == sumOfProperDivisors(b):
        return True
    else:
        return False

def euler_21():
    accum = 0
    for n in range(2, 10000):
        if isAmicable(n):
            accum += n
    return accum


def main():
    print(timing_function(euler_21))

main()

#######################
########################
def NumberAmicable(a : int) -> int:
    b = sumOfProperDivisors(a)
    if b == 0:
        return 0
    if a == sumOfProperDivisors(b):
        return b
    else:
        return 0
    
def amicable(a : int, b: int) -> bool:
    def d(a):
        ls = divisors(a)
        ls.pop()
#        return sum(ls)
    return d(a) == b and a == d(b) and a != b

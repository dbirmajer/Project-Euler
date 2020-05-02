from timing import timing_function
from arithmetic import sumOfPowerDigits
from typing import List


def isSumOfPowersDigits(n, p):
    return n == sumOfPowerDigits(n, 5)

def upperBound(d : int = 2):
    n = sumOfPowerDigits(int('9'*d), 5)
    while n >= 10**d:
        d += 1
        n = sumOfPowerDigits(int('9'*d), 5)
    return n
    
def euler_30():
    ub = upperBound()
    accum = 0
    for n in range(2, ub + 1):
        if isSumOfPowersDigits(n, 5):
#            print(n)
            accum += n
    return accum

def main():
    print(timing_function(euler_30))

main()


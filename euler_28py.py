from timing import timing_function
from arithmetic import primes, isPrime
from typing import List

def ulam(n):
    """
a(4n) = 4n^2 + 2n + 1; a(4n+1) = 4n^2 + 4n + 1; a(4n+2) = 4n^2 + 6n + 3; a(4n+3) = 4n^2 + 8n + 5.
    """
    r = n % 4
    q = (n - r) / 4
    if r == 0:
        return int(4*q**2 +  2*q + 1)
    elif r == 1:
        return int(4*q**2 +  4*q + 1)
    elif r == 2:
        return int(4*q**2 +  6*q + 3)
    else:
        return int(4*q**2 +  8*q + 5)


def spiral(n):
    k = (n + 1) // 2
    m = 4*k - 3
    aux = 0
    for i in range(1, 4*k - 2):
        aux += ulam(i)
    return aux


def euler_28():
    return spiral(1001)

def main():
    print(timing_function(euler_28))

main()


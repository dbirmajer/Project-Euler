#!/usr/bin/env python3
from timing import timing_function
from arithmetic import divisors, triangular

def euler_12():
    n = 1
    while len(divisors(triangular(n))) <= 500:
        n += 1
    return triangular(n)


def main():
    print(timing_function(euler_12))

main()


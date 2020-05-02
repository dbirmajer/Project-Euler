from timing import timing_function
from arithmetic import divisors, triangular
from typing import List
import functools


def euler_22():
    lss = [] 
    with open("euler_22.txt", 'r') as f:
        names = f.read().split(',')
        names.sort()
    accum = 0
    for i in range(len(names)):
        accum += (i+1) * value(names[i])
    return accum


def value(s : str) -> int:
    """Returns the alphabetical value of a string"""
    return sum([ord(c.upper()) - 64 for c in s if c.isalpha()])
        


def main():
    print(timing_function(euler_22))

main()


from timing import timing_function
from arithmetic import divisors, triangular
from typing import List
import functools


def euler_18():
    lss = [] 
    with open("euler_18.txt", 'r') as f:
        line = f.readline().rstrip()
        while line:
            lss.append([int(s) for s in line.split()])
            line = f.readline().rstrip()
        lss.reverse()
        for i in range(len(lss) - 1):
            combine(lss[i], lss[i+1])
        return lss[-1][0]


def combine(rs: List[int], ls: List[int],) -> List[int]:
    """Destroys the second parameter (shorter list)"""
    if not len(rs) > len(ls):
        raise ValueError("The first list parameter must be longer than the second")
    for i in range(len(ls)):
        ls[i] = ls[i] + max(rs[i], rs[i+1])
        


def main():
    print(timing_function(euler_18))

main()


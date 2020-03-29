#!/usr/bin/env python3

#from iterators import Fibs

def euler_02 (ub):
    a = 0
    b = 1
    accum = 0
    while a < ub:
        if a % 2 == 0:
            accum += a
            a, b = b, a + b
    return accum

def main ():
    print ( euler_02 (4000000) )

    main ()

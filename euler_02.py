#!/usr/bin/env python3

import time
from iterators import Fibs
from timing import timing_function

def euler_02(ub):
    a = 0
    b = 1
    accum = 0
    while a < ub:
        if a % 2 == 0: accum += a
        a, b = b, a + b
    return accum

def euler_02_iter(ub):
    fibs = Fibs()
    fib = next(fibs)
    accum = 0 
    while fib < ub:
        if fib % 2 == 0: accum += fib
        fib = next(fibs)
    return accum

def genFibonacci():
    a = 0
    b = 1
    yield a
    while True:
        a, b = b, a + b
        yield a

def euler_02_yield(gen, ub):
    fib = next(gen)
    accum = 0 
    while fib < ub:
        if fib % 2 == 0:
            accum += fib
        fib = next(gen)
    return accum

def accumWhile(gen, go_condition, filter_condition = lambda x : x):
    accum = 0
    g = next(gen)
    while go_condition(g):
        if filter_condition(g) == 0:
            accum += g
        g = next(gen)
    return accum

def nth(gen, n):
    count = 0
    while count < n:
        next(gen)
        count += 1
    return next(gen)

start = time.time()
answer = euler_02_yield(genFibonacci(), 4*10**6)
print(accumWhile(genFibonacci(), lambda x: x <= 4*10**6, lambda x : x % 2 == 0))
end = time.time()
print(f'Answer: {answer}')
print(f'Time to complete: {end - start:.4f}s\n')  

def main():
    input = 4*10**6
    timing_function(euler_02, input)
    timing_function(euler_02_iter, input)

main()

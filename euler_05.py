import time
from functools import reduce

import math

def lcm(a : int, b : int) -> int:
    if a == b == 0:
        raise ValueError('Either a or b must be nonZero')
    return a*b // math.gcd(a, b)

def euler_05(n = 20):
    return reduce(lcm, range(1,n+1), 1)

def factorial(n):
    return reduce(lambda x, y: x * y, range(1,n+1), 1)


start = time.time()    
answer = euler_05()
end = time.time()
print(f'Answer: {answer}')
print(f'Time to complete: {end - start:.4f}s\n')  

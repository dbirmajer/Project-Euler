import time
from arithmetic import isPrime

def genPrimes():
    yield 2
    yield 3
    i = 5
    while True:
        if isPrime(i):
            yield i
        i += 2

def accumWhile(gen, go_condition, filter_condition = lambda x : True):
    accum = 0
    g = next(gen)
    while go_condition(g):
        if filter_condition(g):
            accum += g
        g = next(gen)
    return accum

def nthTerm(gen, n, start = 0):
    for _ in range(n - start):
	    next(gen)
    return next(gen)


def euler_10(n):
    return accumWhile(genPrimes(), lambda x: x <= n)


start = time.time()    
answer = euler_10(2*10**6)
#answer = euler_10(10)
end = time.time()
print(f'Answer: {answer}')
print(f'Time to complete: {end - start:.4f}s\n')  
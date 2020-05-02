import time
from arithmetic import isPrime

def euler_07(n = 10001):
    if n == 1:
        return 2
    count = 2
    i = 5
    prime = 3
    while count < n:
        if isPrime(i):
            prime = i
            count += 1
        i += 2
    return prime

start = time.time()    
answer = euler_07()
end = time.time()
print(f'Answer: {answer}')
print(f'Time to complete: {end - start:.4f}s\n')  

def nth(gen, n, start = 0):
    for _ in range(n - start):
	    next(gen)
    return next(gen)
    

def genPrimes():
    yield 2
    yield 3
    i = 5
    while True:
        if isPrime(i):
            yield i
        i += 2

def euler_07_yield(n):
    return nth(genPrimes(), n, 1)


start = time.time()    
answer = euler_07_yield(n = 10001)
end = time.time()
print(f'Answer: {answer}')
print(f'Time to complete: {end - start:.4f}s\n')  


from timing import timing_function
from arithmetic import primes, isPrime

primes = primes(1000)     
while primes[0] <= 40:
    primes.pop(0)

primes.extend([-p for p in primes])

def quadratic(a : int , b : int , n : int):
    return n**2 + a*n + b

def consecutive(a : int , b : int):
    n = 0
    while isPrime(quadratic(a, b, n)):
        n +=1
    return n

def euler_27():
    maxConsecutive = -1
    for a in range(-999, 1000):
        for b in primes:
            aux = consecutive(a, b)
            if aux > maxConsecutive:
                maxA, maxB, maxConsecutive = a, b, aux
    return maxA * maxB
#    return (maxA, maxB, maxA * maxB, maxConsecutive)


def main():
    print(timing_function(euler_27))

main()


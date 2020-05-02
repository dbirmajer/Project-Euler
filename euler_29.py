from timing import timing_function
from arithmetic import primes, isPrime
from typing import List



def euler_29():
    powers = set()
    for a in range(2, 101):
         for b in range(2, 101):
             powers.add(a**b)
    return len(powers)

def main():
    print(timing_function(euler_29))

main()


import time
from arithmetic import divisors, triangular

def chainLength(n):
    count  = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        count += 1
    return count
        
def euler_14(n = 1000000):
    aux = 0 
    for n in range(n+1):
        a = chainLength(n)
        if a > aux:
            aux = a
            value = n
    return value

def main():
        t1 = time.time()
        print(euler_14())
        t2 = time.time()
        print("Time it took to run the function: " + str((t2 - t1)) + " seconds")
main()


from timing import timing_function
from arithmetic import factorial
from typing import List

ns = list(range(10))

def number(j : int, n) -> (int, int):
    i = 0
    q = factorial(j)
    while i * q < n:
        i += 1
    i -= 1
    return (i, n - i * q)
    
def euler_24():
    global ns
    n = 1000000
    j = 9
    ls = list()
    while  ns:
        i, n = number(j, n)
        j -= 1
        ls.append(str(ns.pop(i)))
#        print("n = ", n, "j =", j, "ns = ", ns)
    return "".join(ls)

def main():
    print(timing_function(euler_24))

main()


from timing import timing_function
from arithmetic import fibonacci
from typing import List


def cycle(num : int , den : int , ls : List[int] = []) :
    print(ls)
    if num in ls:
        return len(ls) - ls.index(num)
    else:
        ls.append(num)
        num = nextNum(num, den)
        return cycle(num, den, ls)    
        if num in ls:
            return len(ls) - ls.index(num)
        else:
            ls.append(num)
            num = nextNum(num, den)
            return cycle(num, den, ls)

def nextNum(num: int, den: int) -> int:
    if num == 0:
        return 0
    while num < den:
        num *= 10
    return num % den
    
        
def recurring(num, den):
    def nextNum(num: int, den: int) -> int:
        if num == 0:
            return 0
        while num < den:
            num *= 10
        return num % den

    def cycle(num : int , den : int , ls : List[int]) :
        if num in ls:
            return len(ls) - ls.index(num)
        else:
            ls.append(num)
            num = nextNum(num, den)
            return cycle(num, den, ls)#    print(ls)
            if num in ls:
                return len(ls) - ls.index(num)
            else:
                ls.append(num)
                num = nextNum(num, den)
                return cycle(num, den, ls)
    return cycle(num, den, [])

        
def euler_26():
    sol = 2
    for d in range(2, 1000):
        if recurring(1, d) > recurring(1, sol):
            sol = d
    return sol

def main():
    print(timing_function(euler_26))

main()


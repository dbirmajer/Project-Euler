from timing import timing_function
from arithmetic import sumOfDigits

def wordLength(n : int) -> int:
    if n in [1, 2, 6, 10]:
        return  3
    elif n in [4, 5, 9]:
        return 4
    elif n in [3, 7, 8, 40, 50, 60]:
        return 5
    elif n in [11, 12, 20, 30, 80, 90]:
        return 6
    elif n in  [15, 16, 70]:
        return 7
    elif n in [13, 14, 18, 19]:
        return 8
    else: ## must be 17
        return 9 

def wordCount(n : int) -> int:
    r = n % 10
    s = n % 100 
    if n <= 20:
        return wordLength(n)
    elif n < 100 and r == 0:
        return wordLength(n)
    elif n < 100:
        return wordLength(n - r) + wordLength(r)
    elif n < 1000 and s == 0:
        return wordLength(n // 100) + len("hundred")
    elif n < 1000:
        return wordCount (n - s) + len("and") + wordCount(s)
    else:
        return wordCount(1) + len("thousand")
    
def euler_17():
    return sum([wordCount(n) for n in range(1,1001)])

def main():
    print(timing_function(euler_17))

main()

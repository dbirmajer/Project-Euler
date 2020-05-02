from timing import timing_function
from arithmetic import sumOfDigits, factorial

def euler_20():
    return sumOfDigits(factorial(100))

def main():
    print(timing_function(euler_20))

main()

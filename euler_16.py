from timing import timing_function
from arithmetic import sumOfDigits

def euler_16():
    return sumOfDigits(2**1000)

def main():
    print(timing_function(euler_16))

main()

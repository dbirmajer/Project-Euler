from timing import timing_function
from arithmetic import binomial

def euler_15():
    return binomial(20 + 20, 20)

def main():
    print(timing_function(euler_15))

main()

from timing import timing_function
from arithmetic import fibonacci

def euler_25():
    i = 0
    x = fibonacci(i)
    while x < 10**999:
        x = fibonacci(i)
        i += 1
    return i - 1

def main():
    print(timing_function(euler_25))

main()


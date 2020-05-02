from timing import timing_function
from arithmetic import divisors, triangular

def euler_13():
    accum = 0 
    with open("euler_13.txt", 'r') as f:
        line = f.readline().rstrip()
        while line:
            accum +=int(line)
            line = f.readline().rstrip()
        return str(accum)[0:10]

def main():
    print(timing_function(euler_13))

main()


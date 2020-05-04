import time
import generators as gen

def euler_10(n):
    return gen.accumWhile(gen.genPrimes(), lambda x: x <= n)


start = time.time()    
#answer = euler_10(2*10**6)
answer = euler_10(10)
end = time.time()
print(f'Answer: {answer}')
print(f'Time to complete: {end - start:.4f}s\n')  

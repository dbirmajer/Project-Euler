import time

def euler_06 (n : int = 100 ) -> int:
    a = sum(map(lambda x : x**2, range(1, 101)))
    return sum(range(1, 101))**2 - a
    

start = time.time()    
answer = euler_06()
end = time.time()
print(f'Answer: {answer}')
print(f'Time to complete: {end - start:.4f}s\n')  



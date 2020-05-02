import time
from arithmetic import digits

from typing import List

def fromDigits(ds : List[int]) -> int:
    return sum([d*10**p for (p, d) in enumerate(reversed(ds))])


digits(123)
fromDigits([1,2,3])
fromDigits(digits(102)) == 102
digits(fromDigits([3,0,2, 4])) == [3,0,2,4]

def isPalindromic(n):
  ds = digits(n)
  return ds == ds[::-1]

def isPalindromicString(n):
  s = str(n)
  return s == s[::-1]

def euler_04():
    ls = [a*b for a in range(100,1000) for b in range(a, 1000)]
    return max(filter(isPalindromic, ls))
#    return max([a*b for a in range(100,1000) for b in range(a, 1000) if isPalindromic(a*b)])

start = time.time()    
answer = euler_04()
end = time.time()
print(f'Answer: {answer}')
print(f'Time to complete: {end - start:.4f}s\n')  
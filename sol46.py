from gauss import is_prime
from gauss import primes

def is_square(n):
    return int(n**.5) == n**.5

n = 33
brk = 0

while 1:
    if not is_prime(n):
        conj = 0
        for prime in primes(2, n):
            if is_square((n - prime)/2):
                conj = 1
    if not conj:
        print n
        break
    n += 2
        

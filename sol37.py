from gauss import primes
from gauss import is_prime

l = []

def trunl(n):
    res = []
    strn = str(n)
    for i in xrange(1, len(strn)):
        res.append(int(strn[:i]))
    return res

def trunr(n):
    res = []
    strn = str(n)
    for i in xrange(1, len(strn)):
        res.append(int(strn[-i:]))
    return res

for prime in primes(8, 10000000):
    if [1 for i in trunl(prime) if is_prime(i)] == [1]*(len(str(prime))-1):
        if [1 for i in trunr(prime) if is_prime(i)] == [1]*(len(str(prime))-1):
            l.append(prime)
        else:
            continue
    else:
        continue
    if len(l) == 11:
        print sum(l)
        break


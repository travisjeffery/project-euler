from operator import mul
from math import sqrt as msqrt

def primes(min, max):
    plist = [2]
    if 2 >= min: yield 2
    i = 3
    while i <= max:
        for p in plist:
            if not i % p or p**2  > i: break
        if i % p:
            plist.append(i)
            if i>= min: yield i
        i += 2

def factors(n):
    for p in primes(2, n):
        if not n % p:
            n = n / p
            yield p
        if n == 1:
            raise StopIteration

def prod(lst):
    return reduce(mul, lst)

def gcd(x, y):
    rem = x % y
    if rem == 0:
        return y
    else:
        return gcd(y, rem)

def sqrt(sqr):
    rt = msqrt(sqr)
    if int(rt) == rt:
        return int(rt)
    else:
        return 0

def pythtrips(max):
    for m in range(2, max):
        for n in range(1, m):
            if not m & 1 and not n & 1:
                continue
            h = sqrt(n**2+m**2)
            if not h:
                continue
            if gcd(m, n) != 1:
                continue
            yield (n,m,h)

import operator

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
    return reduce(operator.mul, lst)

from operator import mul
from math import sqrt as msqrt
from math import factorial

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

def appendseqs(seqs, seqs1):
    result=[]
    if not seqs:
        for seq1 in seqs1:
            result.append([seq1])
    else:
        for seq1 in seqs1:
            result += [seq + [seq1] for seq in seqs]
    return result

def cartprod(l):
    return reduce(appendseqs,l,[])
    
def primefacts(n):
    i = 2
    while i <= n**.5:
        if n % i == 0:
            l = primefacts(n/i)
            l.append(i)
            return l
        i+=1
    return [n]

def facts(n):
    p = primefacts(n)
    factors={}
    for p1 in p:
        try:
            factors[p1]+=1
        except KeyError:
            factors[p1]=1
    return factors

def divisors(n):
    factors = facts(n)
    divs = []
    exps = [map(lambda x: k**x, xrange(0, factors[k]+1)) for k in factors.keys()]
    lfacts = cartprod(exps)
    for f in lfacts:
        divs.append(reduce(lambda x, y: x*y, f, 1))
    divs.sort()
    return divs

def choose(n, k):
    return factorial(n)/(factorial(n-k)*factorial(k))

def pascal(n):
    if n == 1:
        return [[1]]
    else:
        result = pascal(n-1)
        erow = result[-1]
        result.append([(x+y) for x, y in zip([0]+erow, erow + [0])])
        return result

def printpascal(tree):
    if len(tree) == 0: return ''
    line = '    ' * len(tree)
    for cell in tree[0]:
        line += '   %2i' % cell
    return line + '\n' + printpascal(tree[1:])
 
def pascal(n):
    if n == 1:
        return [[1]]
    else:
        result = pascal(n-1)
        erow = result[-1]
        result.append([(x+y) for x,y in zip([0]+erow, erow+[0])])
        return result
 
def pascalpri(tree):
    if len(tree) == 0: return ''
    line = '  ' * len(tree)
    for cell in tree[0]:
        line += '  %2i' % cell
    return line + '\n' + pascalpri(tree[1:])
 

def perms(str):
    if len(str) <= 1:
        yield str
    else:
        for perm in perms(str[1:]):
            for i in xrange(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def permsl(l):
    if len(l) <= 1:
        yield [l]
    yield [p[:i]+[l[0]]+p[i:] for i in xrange(len(l)) for p in permsl(l[1:])]

memo= {0:0, 1:1}
def fib(n):
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
    
def fact(n): return reduce(lambda x,y:x*y,range(1,n+1),1)

def is_perm(a,b): return sorted(str(a)) == sorted(str(b))

def is_palindromic(n): return str(n)==str(n)[::-1]

def is_pandigital(n, s=9): n=str(n);return len(n)==s and not '1234567890'[:s].strip(n)

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def trial_division(n, bound=None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n%p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m*m <= n:
        if n%m == 0:
            return m
        m += dif[i%8]
        i += 1
    return n

def factor(n):
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = trial_division(n)
        e = 1
        n /= p
        while n%p == 0:
            e += 1; n /= p
        F.append((p,e))
    F.sort()
    return F

def gcd(a, b):
    if a < 0:  a = -a
    if b < 0:  b = -b
    if a == 0: return b
    if b == 0: return a
    while b != 0: 
        (a, b) = (b, a%b)
    return a

def binomial(n, k):
    nt = 1
    for t in range(min(k, n-k)):
        nt = nt*(n-t)//(t+1)
    return nt
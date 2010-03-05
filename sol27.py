from gauss import primes, is_prime

def f(a, b, n):
    return (n**2 + (a*n) + b)

def seq_primes(a, b):
    n = 0
    prime = True
    while prime:
        prime = is_prime(f(a,b,n))
        n += 1
    return n-1
    
def gen_primes(n):
    return [x for x in xrange(n) if is_prime(x)]
    
upb = 0
lprimes = gen_primes(1000)
for i in lprimes:
    for j in lprimes:
        l = seq_primes(i, j)
        if l > upb:
            upb = l
            nums = (i, j)
        l = seq_primes(-i, j)
        if l > upb:
            upb = l
            nums = (-i, j)

print("%d" % (nums[0] * nums[1]))

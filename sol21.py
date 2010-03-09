from gauss import divisors

def d(n):
    return sum(divisors(n)[:-1])

print sum(set([i for i in xrange(1, 10001) if i == d(d(i)) and d(i) != i]))
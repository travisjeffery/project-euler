from operator import mul
n = ''

for i in xrange(0, 1000001):
    n += str(i)

print reduce(mul, [int(n[10**i]) for i in xrange(0, 7)])

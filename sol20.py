from math import factorial

n = factorial(100)

print sum([int(str(n)[x]) for x in xrange(len(str(n)))])

n = 2**1000

print sum([int(str(n)[i]) for i in xrange(0, len(str(n)))])

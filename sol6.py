sumsq = 0
sqsum = 0
for i in xrange(1, 101):
    sumsq += i**2
    sqsum += i

print sqsum ** 2 - sumsq


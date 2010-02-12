import math

n = 0
for i in xrange(1,1000):
    if not i % 5 or not i % 3:
        n += i

print n


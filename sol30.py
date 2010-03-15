l = 0

for i in xrange(2, 1000000):
    if i == sum([int(j)**5 for j in str(i)]):
        l += i

print l

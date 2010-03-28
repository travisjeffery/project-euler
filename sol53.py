from gauss import choose

n = 0

for i in xrange(1,101):
    for j in xrange(1, i):
        if choose(i, j) > 1000000:
            n += 1

print n
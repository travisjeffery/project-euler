d = {}

for i in xrange(1, 1001):
    for j in xrange(1, 1001):
        ij = (i**2 + j**2)**.5
        tot = i+j+int(ij)
        if int(ij) == ij and tot <= 1000:
            if tot not in d:
                d[tot] = 1
            else:
                d[tot] += 1

print max([(j, i) for i, j in d.iteritems()])[1]

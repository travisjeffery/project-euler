l = []

for i in xrange(2, 101):
    for j in xrange(2, 101):
        l.append(i**j)

print len(set(l))

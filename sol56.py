sup = 0

for a in xrange(1, 100):
    for b in xrange(1, 100):
        tot = sum([int(l) for l in str(a**b)])
        if tot > sup:
               sup = tot

print sup

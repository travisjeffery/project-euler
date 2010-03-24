from gauss import primes
from gauss import perms

lprimes = list(primes(1000, 10000))

def is_add_seq(x, y, z):
    return z - y == y - x

i = 0
for x in xrange(1, len(lprimes)):
    a = lprimes[x]
    lperms = list(perms(str(a)))
    for y in xrange(x+1, len(lprimes)):
        b = lprimes[y]
        if not str(b) in lperms:
            continue
        for z in xrange(y+1, len(lprimes)):
            c = lprimes[z]
            if not str(c) in lperms:
                continue
            if is_add_seq(a, b, c):
                i += 1
                if i == 2:
                    print "%s%s%s" % (a, b, c)


from lib import divisors

def d(n):
    return sum(divisors(n)[:-1])

tot = []
for i in xrange(1, 10001):
    if i == d(d(i)) and d(i) != i:
        tot.append(i)
        tot.append(d(i))

print sum(set(tot))

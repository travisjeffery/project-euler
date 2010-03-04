from lib import divisors

def d(n):
    return divisors(n)[:-1]

def genabunds(n):
    abund = []
    for i in xrange(1, n+1):
        sum_pds = sum(d(i))
        if sum_pds > i:
            abund.append(i)
    return abund

abunds = genabunds(28124)
sums = set()

for i in xrange(len(abunds)):
    for j in range(i, len(abunds)):
        k = abunds[i] + abunds[j]
        if k < 28124:
            sums.add(k)

print sum(set(xrange(28124))-set(sums))


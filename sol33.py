from fractions import Fraction
from decimal import Decimal
from operator import mul

def samenum(n, n1):
    if set(str(n)).intersection(set(str(n1))):
        return True

def removenum(n, n1):
    strn = str(Decimal(n))
    strn1 = str(Decimal(n1))
    for i in set(str(n)).intersection(set(str(n1))):
        strn = strn.replace(i, "")
        strn1 = strn1.replace(i, "")
    if strn.isdigit() and strn1.isdigit():
        return int(strn), int(strn1)
    else:
        return 0, 0

l = []
for i in xrange(1, 99):
    for j in xrange(i, 100):
        if samenum(i, j):
            n, n1 = removenum(i, j)
            if n != 0 and n1 != 0:
                if float(n)/n1 == float(i)/j and i % 10 and j % 10 != 0:
                    l.append(Fraction(n, n1))

print str(reduce(mul, l)).split('/')[1]

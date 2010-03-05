from gauss import divisors

i = 1

while 1:
    i += 1
    l = sum(xrange(1, i))
    if len(list(divisors(l))) > 500:
        print l
        break

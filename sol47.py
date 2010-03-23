from gauss import primefacts

c = 1
n = 2*3*5*7
while c != 5:
    n += 1
    if len(set(primefacts(n))) == 4:
        c += 1
    else:
        c = 1
        l = []
print n-3

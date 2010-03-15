from gauss import factorial

s = 0

for i in xrange(3, 100000):
    if i == sum([factorial(int(n)) for n in str(i)]):
        s += i
    
print s
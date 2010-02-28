import operator

a,b,c=0,0,0

for m in range(0, 100):
    for n in range(0, 100):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if a + b + c == 1000:
            if a > 0 and b > 0 and c > 0:
                print reduce(operator.mul, [a,b,c])
                break

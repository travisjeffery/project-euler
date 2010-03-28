n = 1
while 1:
    t = 1
    for i in xrange(2, 7):
        if set(str(i*n)) != set(str(n)):
            t = 0
            break
    if t:
        print n
        break
    n += 1

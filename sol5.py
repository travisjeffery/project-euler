def sol5():
    i = 20
    while True:
        for n in xrange(1,21):
            if not i % n and n == 20:
                return i
            if not i % n:
                continue
            if i % n:
                i += 20
                break
print sol5()

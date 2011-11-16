print map(lambda n: (n*(n+1)/2), [100])[0]**2 - sum(map(lambda x: x**2, [i for i in xrange(1, 101)]))


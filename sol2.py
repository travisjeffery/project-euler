def fib():
    x,y = 0,1
    while True:
        yield x
        x,y = y, x+y

def even(seq):
    for n in seq:
        if not n % 2:
            yield n

def under_million(seq):
    for n in seq:
        if n > 10000000:
            break
        yield n

print sum(even(under_million(fib())))

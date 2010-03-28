from gauss import is_palindromic

def is_lychrel(n):
    t = 1
    for i in xrange(1, 50):
        n += int(str(n)[::-1])
        if is_palindromic(n):
            t = 0
            break
    return t

tot = 0
for i in xrange(1, 10000):
    if is_lychrel(i): tot += 1

print tot



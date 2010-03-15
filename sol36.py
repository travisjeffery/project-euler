from gauss import (is_palindromic, base_change)

s = 0
for n in xrange(1, 1000000):
    if is_palindromic(n) and is_palindromic(base_change(n, 2)):
        s += n

print s


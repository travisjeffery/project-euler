from gauss import primes
from gauss import perms

tot = 0
lprimes = list(primes(2, 17))
i = 1

for perm in perms('0123456789'):
    while i < 8:
        if int("".join(perm[i:i+3])) % lprimes[i-1]:
            i = 1
            break
        i += 1
    if i == 8: tot += int(perm)
    i = 1

print tot
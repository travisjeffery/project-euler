from lib import primes

for p in reversed(list(primes(2, 1000))):
    c = 1
    while (pow(10, c) - 1) % p != 0:
        c += 1
    if (p-c) == 1:
        break
print p

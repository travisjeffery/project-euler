from gauss import is_prime
from gauss import primes

plist = list(primes(2, 1000000))

def circular(n, l=[]):
    circ = int(str(n)[-1]+str(n)[:len(str(n))-1])
    while 1:
        if not is_prime(circ):
            return 0
        if circ == n:
            return 1
        circ = int(str(circ)[-1]+str(circ)[:len(str(circ))-1])

optimus = 0
for p in plist:
    if circular(p):
        optimus += 1

print optimus

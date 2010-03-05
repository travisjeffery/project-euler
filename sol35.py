from lib import primes
from lib import perms

pl = [i for i in list(primes(2, 1000000))]

for i in pl:
    print list(perms(str(i)))
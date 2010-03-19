from gauss import is_prime
from gauss import perms

sup = 0
digs = '987654321'

while 1:
    for perm in perms(digs):
        if is_prime(int(perm)):
            if int(perm) > sup:
                sup = int(perm)
    digs = digs.replace(digs[0], '')
    if sup: print sup; break

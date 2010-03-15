from gauss import perms

l = []
permsl = list(perms("123456789"))
for perm in permsl:
    if int(perm[:1]) * int(perm[1:5]) == int(perm[5:]) or \
    int(perm[:2]) * int(perm[2:5]) == int(perm[5:]):
        l.append(int(perm[5:]))


print sum(set(l))
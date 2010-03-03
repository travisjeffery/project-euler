def seq(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

num = upb = 0

done = {1:1}

for i in range(1, 1000000, 2):
    res = i
    nterms = 0
    while res != 1:
        if done.has_key(res):
            nterms += done[res]
            break
        else:
            nterms += 1
            res = seq(res)
    done[i] = nterms
    if nterms > upb:
        num = i
        upb = nterms

print num


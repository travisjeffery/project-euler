def trifn(n):
    return n*(n+1)/2

def penfn(n):
    return n*(3*n-1)/2

def hexfn(n):
    return n*(2*n-1)

n = 143
tris = []
pens = []
hexs = []
while 1:
    tris.append(trifn(n))
    hexs.append(hexfn(n))
    pens.append(penfn(n))
    if trifn(n) in hexs and trifn(n) in pens:
        if trifn(n) == 40755:
            n += 2
            continue
        print trifn(n)
        break
    n += 2

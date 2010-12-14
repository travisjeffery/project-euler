from math import sqrt

def is_pentagonal(n):
	p = (sqrt(1+24*n)+1)/6
	return p == int(p)
	
i = 0
pent = [1]
stop = 0
while 1:
	i += 1
	pent.append(int(i*(3*i-1)*.5))
	for j in xrange(2, len(pent)-1):
		if is_pentagonal(pent[i]-pent[j]) and is_pentagonal(pent[i]+pent[j]):
			print pent[i]-pent[j]
			stop = 1
			break
	if stop: break


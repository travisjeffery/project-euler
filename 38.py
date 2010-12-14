set_pandigital = set([str(i) for i in xrange(1, 10)])

def equal_sets(s1, s2):
	if s1.issubset(s2) and s2.issubset(s1):
		return 1

def is_pandigital(n):
	set_n = set(n)
	if equal_sets(set_n, set_pandigital):
		return 1
		
for x in xrange(9876, 9123, -1):
	n = str(x*1) + str(x*2)
	if is_pandigital(n):
		print n
		break
ways = 0

for a in xrange(41):
	for b in xrange(21):
		for c in xrange(11):
			for d in xrange(5):
				for e in xrange(3):
					for g in xrange(2):
						tot = a*5+b*10+c*20+d*50+e*100+g*200
						if tot <= 200:
							ways += (200 - tot)//2 + 1

print ways
import string

def triangle_nums(n):
	n0 = 1
	while n0 < n:
		yield int(.5*n0*(n0+1))
		n0 +=1

def triangle_nums1(halt):
	n = 1
	prev = 1
	while prev <= halt:
		prev = int(.5*n*(n+1))
		yield prev
		n += 1

def build_alphabet_dict():
	a = {}
	i = 1
	for letter in string.ascii_uppercase:
		a[letter] = i
		i +=1
	return a

a = build_alphabet_dict()
f = open('words.txt', 'r')
fileTotal = 0

for line in f:
	for word in line.split(","):
		wordTotal = 0
		for letter in word.strip('""'):
			wordTotal += a[letter]
		for i in triangle_nums1(wordTotal):
			if wordTotal == i:
				fileTotal += 1

print fileTotal
		
f.close()
s = open("24_7.txt").readline().strip()

def isVowel(n):
	return n in "AEIUOY"

c = 0
m = -1

for i in range(len(s) - 1):
	if isVowel(s[i]) != isVowel(s[i+1]):
		c+=1
	else:
		c = 1

	m = max(m,c)

print(m)

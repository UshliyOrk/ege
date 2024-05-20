s = open('24_8.txt').readline().strip()
c = 0
m =- 1
for i in range(len(s)-2):
	if s[i] in "ABCDEF" and \
	s[i+1] in "ABCDEF" and s[i+2] in "ABCDEF" :
		c = 2
	else: c += 1

	if c > m: m = c

print(m)


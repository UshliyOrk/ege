s = open("24_10.txt").readline().strip()
c = 0
m = -1

for i in range(len(s)-1):
	if s[i] in "XYZ" and s[i+1] in "XYZ": c = 1
	else: c += 1

	if c > m: m = c

print(m)


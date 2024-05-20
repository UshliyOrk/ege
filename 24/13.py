s = open('24_13.txt').readline().strip()

"""
for i in "24": s = s.replace(i, "x")
for i in "135": s = s.replace(i, "y")
s = s.replace("xy", "*")
s = s.replace('x',"|")
s = s.replace('y',"|")
res = s.split("|")
print(max([len(i) for i in res]))
"""

def isEven(n):
	return n in "24"

i=0
c=0
m=-1
while i < len(s)-1:
	if isEven(s[i]) and not isEven(s[i+1]):
		i+=2
		c+=1
	else:
		m = max(m,c)
		c = 0
		i+=1
print(m)

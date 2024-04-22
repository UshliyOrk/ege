s = open("24_6.txt").readline().strip()

for i in "ABCD":
	s = s.replace(i, "*")

m = max([len(i) for i in s.split("*")])

print(m)

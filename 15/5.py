p = list(range(10, 41))
q = list(range(5, 16))
r = list(range(35, 51))

A = []

for x in range(0, 100):
	if not(((x in A) or (x in p)) or ((x in q) <= (x in r))):
		A.append(x)

print(len(A))

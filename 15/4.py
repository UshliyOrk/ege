p = list(range(8,40))
q = list(range(23, 59))
A = []

for x in range(0,81):
	if not(((x in p) or (x in A)) <= ((x in q) or (x in A))):
		A.append(x)

print(len(A))

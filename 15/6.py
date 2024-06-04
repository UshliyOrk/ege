p = list(range(10, 36))
q = list(range(17, 49))

A = list(range(0, 51))

for x in range(0, 51):
	if not(((x in A) >= (not x in p)) <= ((x in A) <= (x in q))):
		A.remove(x)

print(len(A))

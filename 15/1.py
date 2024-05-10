def _del(n, m):
	return n%m == 0

for A in range(500):
	flag = False

	for x in range(1, 500):
		if not((_del(x,10) and _del(x,26) and (x>=300)) <= (A<=x)):
			flag=True
			break

	if not(flag):
		print(A)
		

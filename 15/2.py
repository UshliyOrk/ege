n=100
for A in range(n):
	flag = True
	for x in range(n):
		for y in range(n):
			if not((x+2*y >A) or (y<x) or (x<30)):
				flag = False
	if flag:
		print(A)
				
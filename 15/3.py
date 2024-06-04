n = 100
for A in range(n):
	flag=True
	for x in range(n):
		if not((A+x < 123) <= (x%5 == 0) <= (x%7 != 0)):
			flag = False
	if flag:
		print(A)
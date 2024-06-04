#((x not in a) or (x**2 <=81)) and ((y**2 > 36) or (y in a))
n = 100
a = list(range(n))

for x in range(n):
	for y in range(n):
		if x**2 > 81 and x in a:
			a.remove(x)
		if y**2 <= 36 and y not in a:
			a.append(y)




print(a)
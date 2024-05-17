def f(a, b, n):
	if a>47 or b>47 or n>3:
		return n==3
	if a>b :
		if n%2 == 1:
			return all([f(a+1, b, n+1), f(a+2, b, n+1), 
				f(a+3, b, n+1), f(a, b*2, n+1)])
		return any([f(a+1, b, n+1), f(a+2, b, n+1), 
			f(a+3, b, n+1), f(a, b*2, n+1)])
	elif b==a:
		if n%2 == 1:
			return all([f(a+1, b, n+1), f(a+2, b, n+1), f(a+3, b, n+1), 
				f(a, b+1, n+1), f(a, b+2, n+1), f(a, b+3, n+1)])
		return any([f(a+1, b, n+1), f(a+2, b, n+1), f(a+3, b, n+1), 
			f(a, b+1, n+1), f(a, b+2, n+1), f(a, b+3, n+1)])
	else:
		if n%2 == 1:
			return all([f(a, b+1, n+1), f(a, b+2, n+1), 
				f(a, b+3, n+1), f(a*2, b, n+1)])
		return any([f(a, b+1, n+1), f(a, b+2, n+1), 
			f(a, b+3, n+1), f(a*2, b, n+1)])

res = []
for x in range(1, 100):
	for y in range(1,100):
		if f(x, y, 0):
			res.append(x+y)
			
print(min(res), max(res))

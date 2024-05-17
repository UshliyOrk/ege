n = 125**5 + 25**9 - 30
def f(n):
	res = ''
	while n > 5:
		res+= str(n%5)
		n = n//5
	res+=str(n)
	return res
print(f(n).count("4"))
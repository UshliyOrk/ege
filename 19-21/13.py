def game (n1, n2, m):
	return n1+n2>=m

def f(n1, n2, m, lim, cur=1):
	if cur>lim:
		return -1

	if any([game(n1+1, n2, m), game(n1*2, n2, m),
		game(n1, n2+1, m), game(n1, n2*2, m)]):
		return 1

	cur+=1
	moves=[
	f(n1+1, n2, m, lim, cur), f(n1*2, n2, m, lim, cur), 
	f(n1, n2+1, m, lim, cur), f(n1, n2*2, m, lim, cur)
	]

	if all([i==1 for i in moves]):
		return 2

	if 2 in moves:
		return 3

	if all([i==1 or i==3 for i in moves]):
		return 4


n=4
for s in range(1, 110):
	if f(13, s, 123, n) == n:
		print(s)
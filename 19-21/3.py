#>442
#+1
#+3
#*2

def game(n,m):
	return n>m

def f(n, m, lim, cur = 1):
	if cur > lim:
		return -1

	if any([game(n+1,m),game(n+3,m),game(n*2,m)]):
		return 1

	moves = [f(n+1, m, lim, cur+1), f(n+3, m, lim, cur+1), f(n*2, m, lim, cur+1)]

	#19
	if all([i==1 for i in moves]):
		return 2
	#20
	if 2 in moves:
		return 3
	#21
	if all([i==1 or i == 3 for i in moves]):
		return 4

n=4
for i in range(1, 443):
	if f(i, 442, n) == n:
		print(i)


#>428
#+5
#*5

def game(n,m):
	return n>m

def f(n, m, lim, cur = 1):
	if cur > lim:
		return -1

	if any([game(n+5, m), game(n*5,m)]):
		return 1

	moves = [f(n+5,m,lim,cur+1), f(n*5,m,lim,cur+1)]

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
for i in range(1, 429):
	if f(i, 428, n) == n:
		print(i)

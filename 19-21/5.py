#<117
#-7
#//3

def game(n,m):
	return n<m

def f(n, m, lim, cur = 1, n19=False):
	if cur > lim:
		return -1

	if any([game(n-7, m), game(n//3,m)]):
		return 1

	moves = [f(n-7,m,lim,cur+1), f(n//3,m,lim,cur+1)]

	#19
	if n19:
		if any([i==1 for i in moves]):
			return 2
		if 2 in moves:
			return 3
	#20
	else:
		if all([i==1 for i in moves]):
			return 2
		if 2 in moves:
			return 3
	#21
		if all([i==1 or i == 3 for i in moves]):
			return 4

n=4
for i in range(117, 10000):
	if f(i, 117, n) == n:
		print(i)

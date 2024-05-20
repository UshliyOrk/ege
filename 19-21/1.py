# +2
# +5
# *4
# >272


def game(n, m):
	return n>m


def f(n, m, lim, cur = 1):
	if cur > lim:
		return -1

	if any([game(n+2, m), game(n+5, m), game(n*4, m)]):
		return 1

	moves=[f(n+2,m,lim,cur+1),f(n+5,m,lim,cur+1),f(n*4,m,lim,cur+1)]

	
	if all([i==1 for i in moves]):
		return 2

	if 2 in moves:
		return 3

	if all([i==1 or i==3 for i in moves]) and moves.count(1) != 3:
		return 4

n=4
for i in range(273):
	if f(i, 272, n) == n:
		print(i)
		break




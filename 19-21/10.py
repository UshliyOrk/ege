#+2
#*5
#+>341
#11
#1-325

def game(n1,n2,m):
	return n1+n2 > m

def f(n1,n2,m,lim, cur=1):
	if cur > lim:
		return -1

	if any([
		game(n1+2,n2,m), game(n1*5,n2,m),
		game(n1,n2+2,m), game(n1,n2*5,m)
		]):
		return 1

	moves = [f(n1+2,n2,m,lim,cur+1),f(n1*5,n2,m,lim,cur+1),
			f(n1,n2+2,m,lim,cur+1),f(n1,n2*5,m,lim,cur+1)]

	#19 all заменить на any
	if all([i==1 for i in moves]):
		return 2

	#20
	if 2 in moves:
		return 3

	#21
	if all([i==1 or i==3 for i in moves]):
		return 4

n=4
for i in range(1,326):
	if f(11, i, 341, n) == n:
		print(i)

#374
#+3
#*2
#27

def game(n1,n2,m):
	return n1 + n2 > m

def f(n1, n2, m, lim, cur=1):
	if cur > lim:
		return -1

	if any([game(n1+3, n2, m), game(n1*2, n2, m),
			game(n1, n2+3, m), game(n1, n2*2, m)]):
		return 1

	moves=[f(n1+3, n2, m, lim, cur+1), f(n1*2, n2, m, lim, cur+1), 
		f(n1, n2+3, m, lim, cur+1),f(n1, n2*2, m, lim, cur+1)]

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
for i in range(1, 348):
	if f(27, i, 374, n) == n:
		print(i)

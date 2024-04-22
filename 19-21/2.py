#>83
#+1
#чет *1.5
#нечет *2

def game(n,m):
	return n>m

def f(n,m,lim,cur=1):
	if cur > lim:
		return -1

	#если четное
	if n%2 == 0:
		if any([game(n+1,m), game(n*1.5,m)]):
			return 1

		moves=[f(n+1,m,lim,cur+1),f(n*1.5,m,lim,cur+1)]
	#если не четное
	elif n%2 != 0:
		if any([game(n+1,m), game(n*2,m)]):
			return 1

		moves=[f(n+1,m,lim,cur+1),f(n*2,m,lim,cur+1)]

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
for i in range(1, 84):
	if f(i, 83, n) == n:
		print(i)
		


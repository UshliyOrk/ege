def game(n1, n2, m):
	return n1 > m or n2 > m

def f(n1, n2, m, lim, cur=1):
	if lim > cur:
		return -1

	if n1 > n2:
		if any([game(n1+1, n2, m), game(n1+2, n2, m), game(n1+3, n2, m), game(n1, n2*2, m)]):
			return 1

		moves = [f(n1+1, n2, m, lim, cur+1), f(n1+2, n2, m, lim, cur+1), f(n1+3, n2, m, lim, cur+1), f(n1, n2*2, m, lim, cur+1)]


		if all([i==1 for i in moves]):
			return 2

		if 2 in moves:
			return 3

		if all([i == 1 or i ==3 for i in moves]):
			return 4
	elif n1 < n2:
		if any([game(n1, n2+1, m), game(n1, n2+2, m), game(n1, n2+3, m), game(n1*2, n2, m)]):
			return 1

		moves = [f(n1, n2+1, m, lim, cur+1), f(n1, n2+2, m, lim, cur+1), f(n1, n2+3, m, lim, cur+1), f(n1*2, n2, m, lim, cur+1)]


		if all([i==1 for i in moves]):
			return 2

		if 2 in moves:
			return 3

		if all([i == 1 or i ==3 for i in moves]):
			return 4
	else:
		if any([game(n1+1, n2, m), game(n1+2, n2, m), game(n1+3, n2, m), game(n1, n2+1, m), game(n1, n2+2, m), game(n1, n2+3, m)]):
			return 1

		moves = [f(n1, n2+1, m, lim, cur+1), f(n1, n2+2, m, lim, cur+1), f(n1, n2+3, m, lim, cur+1), f(n1+1, n2, m, lim, cur+1), f(n1+2, n2, m, lim, cur+1), f(n1+3, n2, m, lim, cur+1)]



		if all([i==1 for i in moves]):
			return 2

		if 2 in moves:
			return 3

		if all([i == 1 or i ==3 for i in moves]):
			return 4


n = 3
for s in range(1, 47):
	if f(13, s, 47, n) == n:
		print(s)


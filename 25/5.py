from fnmatch import fnmatch

def eratosphen(n):
	res = set(range(2,n+1))

	for elem in range(len(res)):
		if elem not in res:
			continue

		e = elem ** 2
		while e <= n:
			if e in res:
				res.remove(e)

			e+=elem
	return res

for i in eratosphen(10**7):
	if fnmatch(str(i), "3?1111*"):
		print(i)

from fnmatch import fnmatch

for i in range(0, 10**10+1, 7777):
	if fnmatch(str(i),"12*567?") and i%2 == 0:
		print(i, i//7777)

from fnmatch import fnmatch

for i in range(1000008513, 10**12+1, 98591):
	if fnmatch(str(i),"12?3*456??9"):
		print(i, i//98591)
from fnmatch import fnmatch

for i in range(0, 10**10+1, 1234):
	if fnmatch(str(i), "4*5*6") and fnmatch(str(i),"?74*68?"):
		print(i, i//1234)

from fnmatch import fnmatch

for i in range(0, 10**8+1, 2025):
	if fnmatch(str(i), "12*34?5"):
		print(i, i//2025)
from fnmatch import fnmatch

for i in range(0, 10**10+1, 21025):
	if fnmatch(str(i), "12*34?5"):
		c=0
		n=0
		for x in str(i):
			if int(x)%2 == 0:
				c+=1
			else:
				n+=1
		if n == c:
			print(i, i//21025)

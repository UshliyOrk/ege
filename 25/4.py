from fnmatch import fnmatch

def isPrime(x):
	for i in range(2, int(x**0.5)+1):
		if x%i == 0:
			return False
		return True

for i in range(2, 10**5+1):
	if isPrime(i) and fnmatch(str(i**2), "1?2*0*2?1"):
		print(i**2)

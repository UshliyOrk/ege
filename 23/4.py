def f(start, end):
	if start == end:
		return 1

	if start > end:
		return 0

	return f(start+1, end) + f(start+3, end) + f(start*3, end)

print(f(3,9)*f(9,27)*f(27,31))

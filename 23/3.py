def f(start, end, flag=False):
	if start == end:
		return 1

	if start > end:
		return 0

	if flag:
		return f(start+2, end)+f(start*3, end)

	return f(start+2,end)+f(start*3,end)+f(start**2,end, True)

print(f(2, 64))

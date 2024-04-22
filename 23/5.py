def f(start, end):
	if start == end:
		return 1

	if start < end:
		return 0

	return f(start-1, end)+f(start-3,end)+f(start//2, end)

print(f(39,19)*f(19,16)*f(16,7))

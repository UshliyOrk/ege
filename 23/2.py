def f(start, end):
	if start == end:
		return 1

	if start < end or start == 20:
		return 0

	return f(start-2, end)+f(start-3, end)+f(start//5, end)

print(f(41,10)*f(10,5))

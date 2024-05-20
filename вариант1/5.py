def f(n):
	res = str(bin(n)[2:])
	n1 = res
	while len(res) < 8:
		res = "0"+res

	r=[]
	for i in res:
		if i == "0":
			r.append("1")
		else:
			r.append("0")
	n2 = "".join(r)
	res = int(n2, 2) - int(n1, 2)
	return res

for i in range(256):
	if f(i) == 133:
		print(i)
		break
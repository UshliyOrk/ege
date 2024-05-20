print("k l m n - f")
for k in 1,0:
	for l in 1,0:
		for m in 1,0:
			for n in 1,0:
				if not(not n or k and not m or (l==m)):
					print(f"{k} {l} {m} {n} - 0")
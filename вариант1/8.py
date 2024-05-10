from itertools import permutations
s="РОСОМАХА"
exceptions = ["ОА", "АО", "ОО", "АА"]
for i in set(permutations("РСМХ")):
	exceptions.append("".join(i)) 
count=0
for w in set(permutations(s)):
	word = "".join(w)
	flag = True
	for i in exceptions:
		if i in word:
			flag=False
	if flag:
		count += 1

print(count)
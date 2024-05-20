c = 0

for line in open("9_3.txt"):
	nums = [int(i) for i in line.split("\t")]
	uniq = [i for i in nums if nums.count(i) == 1]
	_max = max(nums)
	if (len(uniq) < 6 and
		nums.count(_max) == 1 and
		_max > ((sum(nums)-_max)/5)*3):
		c+=1

print(c)

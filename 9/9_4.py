c = 0

for line in open("9_4.txt"):
	nums = [int(i) for i in line.split("\t")]

	uniq = [i for i in nums if nums.count(i) == 1]
	_sum = max(nums)+min(nums)

	if (len(uniq) == 5 and
		_sum*2 <= (sum(nums) - _sum)
		):
		c+=1
print(c)

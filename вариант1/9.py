c = 0

for line in open('9.txt'):
	nums = [int(i) for i in line.split()]
	cnt = nums.count(max(nums))
	unique = [i for i in nums if nums.count(i) == 1]
	if cnt == 1 and len(nums) > len(unique) and ((sum(nums) - max(nums))/ 5)*3 < max(nums):
		c+=1
print(c)

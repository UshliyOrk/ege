k = 20
nums = [int(i) for i in open("27_4-A.txt")]

m = -1
for i in range(len(nums)):
	for j in range(i+k, len(nums)):
		m = max(m, nums[i]+nums[j])

print(m)

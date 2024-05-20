k = 30
nums = [int(i) for i in open("27_12-A.txt")]

m = -1
for i in range(len(nums)):
	for j in range(i+k, len(nums)):
		for l in range(j+k, len(nums)):
			m = max(m, nums[i]+nums[j]+nums[l])

print(m)

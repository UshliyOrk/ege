nums = [int(i.strip()) for i in open("17.txt")]
_max = -100
c = 0
for i in range(len(nums) - 1):
	for k in range(i+1, len(nums)):
		x = nums[i]
		y = nums[k]
		if abs(x-y)%60 == 0:
			c+=1
			if abs(x-y) > _max:
				_max = abs(x-y)

print(c, _max)

nums = [int(i.strip()) for i in open("26_6.txt")]
nums.sort(reverse=True)
c=1
current=nums[0]

for i in nums[1:]:
	if current-i >= 8:
		current = i
		c+=1
print(c, current)
#10000 5000
nums = [[int(j.strip()) for j in i.split()] for i in open("26_8.txt")]
for i in range(len(nums)):
	nums[i].append(((nums[i][0]*nums[i][1])/100))
nums.sort(key=lambda x: (x[2], x[0]), reverse=True)
_sum = 0
for i in range(5000):
	_sum+=nums[i][0]-nums[i][2]
for i in range(5000, len(nums)):
	_sum+=nums[i][0]

print(_sum)
print(min([i[2] for i in nums[:5000]]))
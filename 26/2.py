nums = [[int(j.strip()) for j in i.split()] for i in open("26_2.txt").readlines()]
nums.sort(key= lambda x: (x[1], x[0]))

last = nums[0]
c = 1
events = []
for i in nums:
	if i[0] - last[1] >= 20:
		c += 1
		last = i
		events.append(i)

prev = events[-2]
print(prev)
print(list(filter(lambda x: x[0] > 1236 + 20, nums))[-1][0]-1236)
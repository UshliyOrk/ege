nums = [int(i) for i in open("17_6.txt")]

_min = min(i for i in nums if i%10 == 5 and 99<i<1000)

c=0

s_max = -1

for i in range(len(nums)-1):
	x = nums[i]
	y = nums[i+1]

	xy = x + y

	if(any([99<i<1000 for i in [x, y]]) and
		(xy % _min == 0) ):
		c += 1

		if xy > s_max:
			s_max = xy

print(c, s_max)

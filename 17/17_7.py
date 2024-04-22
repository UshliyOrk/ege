nums = [int(i) for i in  open("17_7.txt")]
_min = [abs(i) for i in nums]
_min = min(_min)
_max = -9999999
c=0

for i in range(len(nums)-1):
	x = nums[i]
	y = nums[i+1]

	s = str(x)[0]+str(y)[0]

	if (s.count('-') == 1 and 
		x+y > 0 and  
		(x+y)%_min == 0):
		c+=1
		if x+y > _max:
			_max = x+y

print(c, _max)


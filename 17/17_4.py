nums =[int(i) for i in open("17_4.txt")]
c=0
_max=[i for i in nums if str(abs(i))[0] == "8"]
_max=max(_max)
_min=99999999

for i in range(len(nums)-2):
	x = nums[i]
	y = nums[i+1]
	z = nums[i+2]
	s = str(abs(x))[0]+str(abs(y))[0]+str(abs(z))[0]
	if s.count('6') <= 1 and x+y+z >= _max:
		c+=1
		if x+y+z <= _min:
			_min = x+y+z

print(c, _min)


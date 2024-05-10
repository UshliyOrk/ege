nums = [int(i) for i in open("17_5.txt")]
_max=-99999
c=0

for i in range(len(nums)-3):
	x=nums[i]
	y=nums[i+3]

	if ((abs(x)%100==13 and abs(y)%100!=13) or 
		(abs(x)%100!=13 and abs(y)%100==13)):
		c+=1
		if x+y >= _max:
			_max=x+y

print(c, _max)
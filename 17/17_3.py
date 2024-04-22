nums = [int(i) for i in open("17_3.txt")]

_max = max(i for i in nums if abs(i)%100 == 18)

c=0

m_max = -(10**100)

for i in range(len(nums)-2):
	x = nums[i]
	y = nums[i+1]
	z = nums[i+2]

	xyz = x*y*z

	if(any([9999<abs(i)<100000 for i in [x, y, z]]) and
		(xyz % _max == 0) ):
		c += 1

		if xyz > m_max:
			m_max = xyz

print(c, m_max)

c = 0

for line in open("9_10.txt"):
	nums = [int(i) for i in line.split("\t")]
	uniq = [i for i in nums if nums.count(i) == 1]
	
	if (len(uniq) == 4 and
		((sum(nums) - sum(uniq)))/2 < (sum(uniq)/4)):
		c+=1

print(c)

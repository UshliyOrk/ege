c = 0

for line in open("9_1.txt"):
	nums = [int(i) for i in line.split("\t")]
	dups = [i for i in nums if nums.count(i) == 2]
	if(
		(len(dups) == 6) and
		((min(dups)+max(dups))/2 < (sum(nums)-sum(dups)))
		):
		c+=1

print(c)

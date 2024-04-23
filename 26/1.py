from math import ceil 

nums = [int(i.strip()) for i in open("26_1.txt").readlines()]
nums.sort()

a = [i for i in nums if i <= 350]
b = [i for i in nums if i > 350]

#1
_sum = sum(a)
i = 0
while i < len(b):
    elems = b[i: i+3]
    min_elem = min(elems)
    _sum += ceil((sum(elems) - min_elem) + min_elem / 4)
    i += 3
print(_sum)

#2
_sum = sum(a)
for i in range(len(b)//3): _sum += b.pop(0)/4

_sum += sum(b)

print(ceil(_sum))
#10000 5000000000

roads = [[int(j.strip()) for j in i.split()] for i in open("26_7.txt")]
roads.sort()

notInterrupted = []
start = roads[0][0]
stop = roads [0][1]

for i in roads[1:]:
	length = range(start, stop+1)
	if i[0] in length and i[1]>stop:
		stop = i[1]
	elif i[0]<start and i[1]>stop:
		stop = i[0]
		start = i[1]
	elif i[0] in length and i[1] in length:
		pass
	else:
		notInterrupted.append([start, stop])
		start = i[0]
		stop = i[1]
notInterrupted.append([start, stop])

print(len(notInterrupted)+1)
print(max([i[1]-i[0] for i in notInterrupted]))

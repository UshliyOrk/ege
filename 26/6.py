films = [[int(j.strip()) for j in i.split()] for i in open('26_9.txt')]
films.sort()

start = films[0][0]
stop = films[0][1]
nonStop = []

for film in films:
	duration = range(start, stop+1)
	if film[0] in duration and  film[1]>stop:
		stop = film[1]
	elif film[0] in duration and film[1] in duration:
		pass
	elif film[0] > stop and film[1] < start:
		start = film[0]
		stop = film[1]
	else:
		nonStop.append(stop-start)
		start = film[0]
		stop = film[1]
nonStop.append(stop-start)

print(sum(nonStop))
print(max(nonStop))

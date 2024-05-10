from turtle import *
screensize(10000, 10000)
tracer(0)
n=20
for i in range(4):
	forward(14*n)
	right(120)
up()

for x in range(-25, 25):
	for y in range(-25,25):
		goto(x*n, y*n)
		dot("red")
exitonclick()
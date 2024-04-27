from turtle import *
tracer(0)
screensize(10000, 10000)

step = 50

right(225)
for i in range(6):
	forward(15*step)
	right(60)
	forward(7*step)
	right(120)

up()
for x in range(-25,25):
	for y in range(-25,25):
		goto(x*step, y*step)
		dot(10, "red")

exitonclick()

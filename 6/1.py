from turtle import *
tracer(0)
screensize(10000, 10000)

step=20
for i in range(2):
	forward(8*step)
	right(90)
	forward(18*step)
	right(90)
up()

forward(4*step)
right(90)
forward(10*step)
left(90)

down()
for i in range(2):
	forward(17*step)
	right(90)
	forward(7*step)
	right(90)	

up()
for x in range(-25,25):
	for y in range(-25,25):
		goto(x*step, y*step)
		dot(5, "red")

exitonclick()

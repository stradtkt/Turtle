import turtle
from turtle import *

DIST = 100
for x in range(0,5):
    print("x", x)
    turtle.speed('normal')
    turtle.fd(30); turtle.dot(10, 'blue'); turtle.fd(30)
    for y in range(1,5):
        print("y", y)
        # turn the pointer 90 degrees to the right
        turtle.fd(30); turtle.dot(10, 'red'); turtle.fd(30)
        turtle.speed('normal')
        turtle.right(20)
        turtle.speed('normal')
        turtle.pensize(5)
        turtle.circle(50); turtle.dot(20, 'green'); turtle.circle(50); turtle.dot(20, 'blue')
        turtle.speed('normal')
        turtle.degrees(40.0)
        turtle.right(90)
        turtle.fd(20)
        turtle.pensize(5)
        turtle.circle(50); turtle.dot(20, 'pink'); turtle.circle(50); turtle.dot(20, 'green')
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20
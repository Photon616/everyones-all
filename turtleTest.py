import turtle
import math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("white")

a = 256
k = 2.0/21

for angle in range(4096):
    theta = math.radians((angle * 4))
    r = a * math.sin(k * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    t.goto(x, y)

turtle.done()
import turtle as t
import math as m

t.shape('turtle')
t.speed(10)
t.pencolor(0,0,0)
t.colormode(255)
t.pensize(100)
t.shapesize(1)
r = 255
g = 0
b = 0

# 255 = 3 * 5 * 17

jugi = 17
delta = 15

while True:
    for j in range(jugi):
        g += delta
        t.pencolor(r,g,b)
        t.forward(1)
    for j in range(jugi):
        r -= delta
        t.pencolor(r,g,b)
        t.forward(1)
    for j in range(jugi):
        b += delta
        t.pencolor(r,g,b)
        t.forward(1)
    for j in range(jugi):
        g -= delta
        t.pencolor(r,g,b)
        t.forward(1)
    for j in range(jugi):
        r += delta
        t.pencolor(r,g,b)
        t.forward(1)
    for j in range(jugi):
        b -= delta
        t.pencolor(r,g,b)
        t.forward(1)
    

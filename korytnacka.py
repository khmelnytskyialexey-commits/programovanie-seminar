import turtle
from random import*
t = turtle.Turtle()
def draw(length,sides):
    for i in range(sides):
        t.color('blue')
        t.pensize(cislo)
        t.forward(length)
        t.right(360/sides)
t.color('blue')
t.pensize(4)
t.begin_fill()
t.end_fill()
t.fillcolor('yellow')
cislo = randint(1,10)
draw(100,6)

turtle.done()

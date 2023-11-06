from turtle import *
from random import *

#Define a cor do background
bgcolor("Teal")
speed(8)
pensize(10)

#Move o cursor aleatoriamente
def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()

#Desenha um quadrilátero    
def square():
    color("Blue")
    pendown()
    right(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    penup()

#Desenha um triângulo
def triangle():
    pendown()
    for count in range(3):
        color("Red")
        back(45)
        left(120)
    penup()


for q in range(15):
    moveToRandomLocation()
    square()

for t in range(15):
    moveToRandomLocation()
    triangle()
    

hideturtle()
done()

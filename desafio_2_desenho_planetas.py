from turtle import *

#Define a cor do background
bgcolor("MidnightBlue")

#A função desenha um planeta


def drawSphere(planetSize, planetColor):
    color(planetColor)
    pendown()
    begin_fill()
    circle(planetSize)
    end_fill()
    penup()
    


#Desenha múltiplas estrelas
drawSphere(30, "Orange")
forward(150)
drawSphere(50, "Red")
left(120)
forward(150)
drawSphere(70, "Teal")

hideturtle()
done()

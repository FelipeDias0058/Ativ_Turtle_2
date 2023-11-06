from turtle import *
from random import *

#Define a cor do background

bgcolor("MidnightBlue")

#Move o cursor para uma posição aleatória
def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()

#A função desenha uma estrela de certo tamanho
def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()


#Desenha múltiplas estrelas
for star in range(30):
    moveToRandomLocation()
    drawStar(randint(5, 25), "White")

hideturtle()
done()

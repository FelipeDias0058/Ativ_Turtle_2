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

#Desenha uma galáxia
def drawGalaxy(numberOfStars):
    starColours = ["#058396", "#0275A6", "#827e01"]
    moveToRandomLocation()

    penup()
    left(randint(-180, 180))
    forward(randint(5, 20))
    pendown()

    drawStar(2, choice(starColours))

#Desenha constelações
def drawConstellations(numberOfStars):
    moveToRandomLocation()

    for star in range(numberOfStars -1):
        drawStar(randint(7, 15), "White")
        pendown()
        left(randint(-90, 90))
        forward(randint(30, 70))
    drawStar(randint(7, 15), "White")

speed(11)

#Desenha múltiplas estrelas
for star in range(30):
    moveToRandomLocation()
    drawStar(randint(5, 25), "White")

for galaxy in range(3):
    drawGalaxy(40)

for constellation in range(2):
    drawConstellations(randint(4, 7))

hideturtle()
done()

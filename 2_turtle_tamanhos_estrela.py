from turtle import *

#Define a cor do cursor e background

bgcolor("MidnightBlue")

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
drawStar(50, "Red")
forward(100)
drawStar(30, "White")
left(120)
forward(150)
drawStar(70, "Green")

hideturtle()
done()

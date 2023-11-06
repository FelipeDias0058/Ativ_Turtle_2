from turtle import *

#Define a cor do cursor e background
color("WhiteSmoke")
bgcolor("MidnightBlue")

#A função desenha uma estrela
def drawStar():
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(50)
    end_fill()
    penup()

def drawSphere():
    speed(120)
    pendown()
    begin_fill()
    for count in range(360):
        forward(1)
        right(1)
    end_fill()
    speed(7)
    penup()
    


#Desenha múltiplas estrelas
drawSphere()
forward(150)
drawSphere()
left(120)
forward(150)
drawStar()

hideturtle()
done()

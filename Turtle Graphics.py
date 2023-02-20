import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)

def pulo (t, x, y):
    'faz tartaruga saltar para coordenadas (x,y)'

    t.penup()
    t.goto(x, y)
    t.pendown()

def carinha (t,x, y):
    t.pensize(3)
    t.setheading(0)

    pulo (t, x, y)
    #fazendo contorno do rosto
    t.circle(100)

    #fazendo olho esquerdo
    pulo(t,x-35,y+120)
    t.dot(25)

    #fazendo olho direito
    pulo(t,x+35, y+120)
    t.dot(25)

    #fazendo sorriso
    pulo(t,x-60.62,y+65)
    t.setheading(-60)
    t.circle(70,120)

carinha(t,100,50)
carinha(t,-120,50)

u = print(input("coe"))



import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)

#fazendo contorno do rostoG
t.circle(100)

#fazendo olho esquerdo
t.penup()
t.goto(-35,120)
t.pendown()
t.dot(25)

#fazendo olho direito
t.penup()
t.goto(35,120)
t.pendown()
t.dot(25)

#fazendo sorriso
t.penup()
t.goto(-60.62,80)
t.pendown()
t.setheading(-60)
t.circle(70,120)


u = print(input("coe"))



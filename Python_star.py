import turtle
star = turtle.Turtle()
screen = turtle.Screen()
screen.setup(500,600, startx=0,starty=450)
star.penup()
star.goto(0,200)
star.pendown()
star.right(75)
star.forward(300)
for i in range(4):
    star.right(144)
    star.forward(300)
turtle.done()
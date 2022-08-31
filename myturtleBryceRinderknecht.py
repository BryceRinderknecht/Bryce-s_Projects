import turtle
screen_width = 800
screen_height = 600
turtle.setup(screen_width, screen_height)
window = turtle.Screen()
window.title('My Turtle')
window.bgcolor('red')
bob = turtle.Turtle()
bob.pensize(3)
turtle.colormode(255)
bob.turtlesize(3,3)
bob.speed(1)
turtle.hideturtle()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()
turtle.penup()
turtle.forward(150)
turtle.pendown()
for x in range(8):
    turtle.forward(25)
    turtle.right(45)
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.pendown()
for x in range(3):
    turtle.forward(25)
    turtle.right(120)
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.pendown()
for x in range(4):
    turtle.forward(25)
    turtle.right(90)
turtle.penup()
#First Turtle Graphics Programming assignment
#Bryce Rinderknecht
#10/28/20
#Write a program that uses turtle graphics
turtle.forward(100)
turtle.pendown()
for x in range(5):
    turtle.forward(25)
    turtle.right(72)
turtle.penup()
turtle.forward(100)
turtle.pendown()
for x in range(6):
        turtle.forward(25)
        turtle.right(60)
turtle.penup()
turtle.forward(100)
turtle.pendown()
for x in range(9):
        turtle.forward(25)
        turtle.right(40)
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.pendown()
for x in range(10):
        turtle.forward(25)
        turtle.right(36)
turtle.penup()
turtle.forward(100)
turtle.pendown()
for x in range(12):
    turtle.forward(25)
    turtle.right(30)
turtle.penup()
turtle.forward(100)
turtle.right(90)
turtle.forward(250)
turtle.pendown()
turtle.pencolor("yellow")
for x in range(18):
    turtle.forward(25)
    turtle.right(20)
turtle.exitonclick()

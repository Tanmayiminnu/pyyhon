import turtle

screen = turtle.screen()
screen.setup(width=600 ,height=600)
screen.bgcolor("lightblue")
screen.title("Drawing a Squre")

pen = turtle.turtle()
pen.color("black")
pen.pensize(3)


for i in range(4):
    pen.forword(100)
    pen.right(90)


turtle.done()
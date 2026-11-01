import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Star ⭐")

star = turtle.Turtle()
star.color("yellow")
star.speed(3)
star.pensize(3)

for i in range(36):
    star.clear()

    for j in range(5):
        star.forward(150)
        star.right(144)

    star.right(10)
    time.sleep(0.1)

turtle.done()

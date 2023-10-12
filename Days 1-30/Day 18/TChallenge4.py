from turtle import Turtle
import random
import turtle

timmy = Turtle()
timmy.pensize(15)
directions = [0 , 90 , 180 , 270]
timmy.speed("fastest")

turtle.colormode(255)
def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    color = (r , g , b)
    return color

while True:
    timmy.color(random_color())
    timmy.forward(50)
    timmy.right(random.choice(directions))
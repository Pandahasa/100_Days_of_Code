from turtle import Turtle
import random
from turtle import exitonclick
import turtle
timmy = Turtle()
timmy.down()
timmy.speed("fastest")
turtle.colormode(255)
def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    color = (r , g , b)
    return color


x = 0
for x in range(360):
    x += 5
    timmy.circle(100)
    timmy.home()
    timmy.right(x)
    timmy.color(random_color())
    
exitonclick()
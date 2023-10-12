from turtle import Turtle

timmy = Turtle()
timmy.down()

for sides in range(3 , 11):
    for x in range(sides):
        timmy.forward(100)
        timmy.right((180-(180*(sides-2))/sides))

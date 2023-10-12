import turtle as t
from turtle import Turtle, Screen, clear

timmy = Turtle()
screen = Screen()

def forward():
    t.fd(10)

def backward():
    t.backward(10)

def counter_clock():
    t.left(15)

def clockwise():
    t.right(15)

screen.listen()
screen.onkeypress(key = "w" , fun = forward)
screen.onkeypress(key = "s" , fun = backward)
screen.onkeypress(key = "a" , fun = counter_clock)
screen.onkeypress(key = "d" , fun = clockwise)
screen.onkeypress(key = "c" , fun = screen.reset)
screen.exitonclick()

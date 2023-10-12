from turtle import Turtle, Screen
import random

race_on = True
s = Screen()
user_bet = s.textinput(title = "Make your bet" , prompt = "Which color turtle will win the race?")
colors = ["red" , "blue" , "orange" , "purple" , "green" , "yellow"]
all_turtles = []

for turtle in range(0 , 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.up()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x = -340 , y = -70 + (turtle * 30))
    all_turtles.append(new_turtle)

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 340:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You win")
            else:
                print("You lose")
        x = random.randint(0 , 10)
        turtle.fd(x)

s.exitonclick()
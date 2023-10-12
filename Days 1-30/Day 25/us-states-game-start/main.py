import csv
import os
import sys
import pandas
import turtle as t

states = os.path.join(sys.path[0], '50_states.csv')
image = os.path.join(sys.path[0], 'blank_states_img.gif')
s = t.Screen()
s.title("U.S. States Game")
s.addshape(image)
t.shape(image)

data = pandas.read_csv(states)
all_state = data.state.to_list()

guessed = []
correct = 0




while correct < 50:
    answer = s.textinput(title = "Guess the State" , prompt = "What is a state's name")

    if answer in all_state:
        state_data = data[data.state == answer]
        correct += 1
        turtle = t.Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(state_data.x) , int(state_data.y))
        turtle.write(answer)
        turtlescore = t.Turtle()
        turtlescore.hideturtle()
        turtlescore.penup()
        turtlescore.goto(-250 , 250)
        turtlescore.clear()
        turtlescore.write(correct)




s.exitonclick()
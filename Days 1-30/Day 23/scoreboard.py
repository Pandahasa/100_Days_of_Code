FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.goto(-250 , 250)
        self.color("black")
        self.level_up()


    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", move=False, align='left', font = FONT)

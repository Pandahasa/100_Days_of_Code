from mimetypes import init
from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0 , 250)
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))


    def score_count(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))
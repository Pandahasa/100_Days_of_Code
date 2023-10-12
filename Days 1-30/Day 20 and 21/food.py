import random
from turtle import Turtle

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5 , stretch_wid= 0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(random.randint(-280 , 280) , random.randint(-280 , 280))
    
    def refresh(self):
        self.goto(random.randint(-280 , 280) , random.randint(-280 , 280))
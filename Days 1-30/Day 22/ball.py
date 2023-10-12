from turtle import Turtle
from paddle import Paddle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.color("white")
        self.left(135)
        print(self.heading())
        
    def move(self):
        self.forward(20)
        if self.ycor() < -280 or self.ycor() > 280:
            if self.heading() == 135 or self.heading() == 315:
                self.left(90)
            elif self.heading() == 225 or self.heading() == 45:
                self.right(90)

        if self.xcor() > 390 or self.xcor() < -390:
            return True
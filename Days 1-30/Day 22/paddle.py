from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.pad1 = Turtle("square")
        self.pad1.color("white")
        self.pad1.shapesize(0.4 , 3)
        self.pad1.seth(90)
        self.pad1.up()
        self.pad1.speed("fastest")
        self.pad1.goto(380 , 0)
        self.pad2 = Turtle("square")
        self.pad2.color("white")
        self.pad2.shapesize(0.4 , 3)
        self.pad2.seth(90)
        self.pad2.up()
        self.pad2.speed("fastest")
        self.pad2.goto(-380 , 0)

    def goup1(self):
        self.pad1.seth(90)
        self.pad1.fd(20)
    
    def godown1(self):
        self.pad1.seth(270)
        self.pad1.fd(20)

    def goup2(self):
        self.pad2.seth(90)
        self.pad2.fd(20)
    
    def godown2(self):
        self.pad2.seth(270)
        self.pad2.fd(20)
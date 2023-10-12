from concurrent.futures.process import _sendback_result
from turtle import Screen , Turtle
import time

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.setup()
        self.head = self.snake_segments[0]

        
    def setup(self):
        for x in range(3):
            segment = Turtle("square")
            segment.up()
            segment.color("white")
            segment.goto(-20 * x , 0)
            self.snake_segments.append(segment)

    def extend(self):
        segment = Turtle("square")
        segment.up()
        segment.color("white")
        xy = self.snake_segments[-1].pos()
        segment.goto(xy)
        self.snake_segments.append(segment)

    def move_forward(self):
        for seg in range(len(self.snake_segments) - 1 , 0 , -1):
            xy = self.snake_segments[seg-1].pos()
            self.snake_segments[seg].goto(xy)
        self.head.forward(20)

    def collision(self):
        for seg in self.snake_segments[1:]:
            if self.head.distance(seg) < 10:
                return True

    def up(self):
        if self.head.heading() == 0:
            self.head.left(90)
        elif self.head.heading() == 180:
            self.head.right(90)
    

    def down(self):
        if self.head.heading() == 0:
            self.head.right(90)
        elif self.head.heading() == 180:
            self.head.left(90)

    def right(self):
        if self.head.heading() == 270:
            self.head.left(90)
        elif self.head.heading() == 90:
            self.head.right(90)

    def left(self):
        if self.head.heading() == 90:
            self.head.left(90)
        elif self.head.heading() == 270:
            self.head.right(90)
            
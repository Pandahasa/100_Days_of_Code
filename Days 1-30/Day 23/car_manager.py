COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.cars = []


    def generate(self):
        if random.randint(1 , 6) == 1:
            car = Turtle("square")
            car.up()
            car.setheading(180)
            car.shapesize(1 , 2)
            car.color(random.choice(COLORS))
            car.goto(300 , random.randrange(-250 , 250))
            self.cars.append(car)

    def move_cars(self , level):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1)))



import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate()
    car.move_cars(score.score)
    screen.listen()
    screen.onkey(player.move_forward , "Up")
    screen.onkey(player.move_backward, "Down")
    for x in car.cars:
        if x.distance(player) < 20:
            game_is_on = False
    if player.ycor() == 280:
        player.start()
        score.level_up()

    

screen.exitonclick()
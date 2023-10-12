from turtle import Screen
import time
from snake import Snake
from food import Food
from score import scoreboard

s = Screen()
s.setup(600 , 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)


snake = Snake()
food = Food()
score = scoreboard()

game_on = True
while game_on:
    s.update()
    time.sleep(0.1)

    snake.move_forward()

    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280 or snake.head.ycor() > 280:
        game_on = False
    if snake.collision():
        game_on = False
    s.listen()
    s.onkey(snake.up , "Up")
    s.onkey(snake.down , "Down")
    s.onkey(snake.left , "Left")
    s.onkey(snake.right , "Right")
    
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_count()
        snake.extend()
    












s.exitonclick()
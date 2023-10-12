from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from score import scoreboard

s = Screen()
s.setup(800 , 600)
s.bgcolor("black")
s.title("PONG Game")
s.tracer(0)
score = scoreboard()
ball = Ball()
paddle = Paddle()
game_on = True

while game_on:
    s.update()
    ball.move()
    time.sleep(0.1)

    s.listen()
    s.onkeypress(paddle.goup1 , "Up")
    s.onkeypress(paddle.godown1 , "Down")
    s.onkeypress(paddle.goup2 , "w")
    s.onkeypress(paddle.godown2 , "s")
    if paddle.pad1.distance(ball) < 20:
            if ball.heading() == 315:
                ball.right(90)
            elif ball.heading() == 45:
                ball.left(90)
    if paddle.pad2.distance(ball) < 20:
            if ball.heading() == 135:
                ball.right(90)
            elif ball.heading() == 225:
                ball.left(90)
    if ball.xcor() == 390 or ball.xcor() == -390:
        score.score_count()


s.exitonclick()
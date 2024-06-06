from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.change_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_down()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_up()

screen.exitonclick()

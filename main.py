from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect wall collision.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detect touch paddle and bounce.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # detect right paddle miss.
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.left_point()
        time.sleep(0.5)

    # detect left paddle miss.
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.right_point()
        time.sleep(0.5)

    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()

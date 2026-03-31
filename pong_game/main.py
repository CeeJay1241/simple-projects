from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350,0))


scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_down, 'Down')
screen.onclick(lambda x, y: screen.bye())

ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    #Detect collision with wall
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Deterct right paddle miss  
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    #Deterct left paddle miss
    if ball.xcor() < -370:
        ball.reset_position() 
        scoreboard.r_point()

screen.exitonclick()
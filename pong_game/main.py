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
r_paddle = Paddle((350, 0))
scoreboard = Scoreboard()
ball = Ball()

left_up_pressed = False
left_down_pressed = False
right_up_pressed = False
right_down_pressed = False


def set_left_up_pressed():
    global left_up_pressed
    left_up_pressed = True


def set_left_up_released():
    global left_up_pressed
    left_up_pressed = False


def set_left_down_pressed():
    global left_down_pressed
    left_down_pressed = True


def set_left_down_released():
    global left_down_pressed
    left_down_pressed = False


def set_right_up_pressed():
    global right_up_pressed
    right_up_pressed = True


def set_right_up_released():
    global right_up_pressed
    right_up_pressed = False


def set_right_down_pressed():
    global right_down_pressed
    right_down_pressed = True


def set_right_down_released():
    global right_down_pressed
    right_down_pressed = False


screen.listen()
screen.onkeypress(set_right_up_pressed, "Up")
screen.onkeyrelease(set_right_up_released, "Up")
screen.onkeypress(set_right_down_pressed, "Down")
screen.onkeyrelease(set_right_down_released, "Down")
screen.onkeypress(set_left_up_pressed, "w")
screen.onkeyrelease(set_left_up_released, "w")
screen.onkeypress(set_left_down_pressed, "s")
screen.onkeyrelease(set_left_down_released, "s")
screen.onclick(lambda x, y: screen.bye())

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    if left_up_pressed:
        l_paddle.go_up()
    if left_down_pressed:
        l_paddle.go_down()
    if right_up_pressed:
        r_paddle.go_up()
    if right_down_pressed:
        r_paddle.go_down()

    # Detect collision with wall
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.x_move > 0 and ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.x_move < 0 and ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle miss
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
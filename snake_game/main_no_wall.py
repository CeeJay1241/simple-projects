from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def save_and_exit():
    if scoreboard.score > scoreboard.high_score:
        scoreboard.high_score = scoreboard.score
        scoreboard.data_file.write_text(f"{scoreboard.high_score}")
    screen.bye()

screen.onclick(lambda x, y: save_and_exit())
scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.move()
        snake.grow()
        scoreboard.level_up()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()
            break


screen.exitonclick()

from turtle import Turtle, Screen
from snake import Snake
import time 

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)



screen.onclick(lambda x, y: screen.bye())

snake = Snake()
screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    













screen.exitonclick()
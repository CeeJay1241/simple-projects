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



screen.onclick(lambda x, y: screen.bye())
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
    time.sleep(0.05)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.move()
        snake.grow()
        scoreboard.level_up()
    
    
    #Detect collision with walls or tail
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 285 or snake.head.ycor() < -280 or snake.head.distance(snake.new_seg) < 5:
        scoreboard.end_game()
        game_on = False
    











screen.exitonclick()
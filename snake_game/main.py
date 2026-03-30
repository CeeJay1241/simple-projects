from turtle import Turtle, Screen
from time import Sleep

sleep = Sleep()
screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for pos in starting_positions:
    new_seg = Turtle("square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(pos)
    segments.append(new_seg)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    for seg_num in range(2, 0, 1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
        















screen.exitonclick()
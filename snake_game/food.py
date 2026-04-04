from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.move()


    def move(self):
        self.x_loc = random.randint(-280, 280)
        self.y_loc = random.randint(-280, 280)
        self.goto(self.x_loc, self.y_loc)


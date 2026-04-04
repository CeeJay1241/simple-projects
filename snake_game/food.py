from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.x_loc = range(-280, 280)
        self.y_loc = range(-280, 280)


    
    def move(self):
        self.goto(random.choice(self.x_loc), random.choice(self.y_loc))
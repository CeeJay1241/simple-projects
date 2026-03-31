from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        #self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.04

    def move(self):
        """Moves the ball along the x and y coordinates"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        """Bounces the ball off the walls"""
        self.y_move *= -1
        
    
    def bounce_x(self):
        """Makes the ball bounce and faster"""
        self.x_move *= -1
        self.move_speed *= 0.85

    def reset_position(self):
        """Restarts the ball in the center and makes it bounce(go in the opposite direction)"""
        self.goto(0,0)
        self.move_speed = 0.04
        self.bounce_x()
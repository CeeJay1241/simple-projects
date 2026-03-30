from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cord):
        self.cord = cord
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(cord)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)
        
    def go_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)

    


        
from turtle import Turtle
MOVE_DISTANCE = 20

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.gen_snake()
        self.head = self.segments[0]
        

    def gen_snake(self):
        for pos in self.starting_positions:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(pos)
            self.segments.append(new_seg)

    def move(self):
        for seg_num in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        self.head.setheading(90)
        
    def turn_left(self):
        self.head.setheading(180)

    def turn_down(self):
        self.head.setheading(270)

    def turn_right(self):
        self.head.setheading(0)

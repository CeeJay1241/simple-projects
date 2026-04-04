from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        """Initialize the snake with its starting segments and head reference."""
        super().__init__()
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.gen_snake()
        self.head = self.segments[0]
        
        

    def gen_snake(self):
        """Create the initial snake body segments at the starting positions."""
        for pos in self.starting_positions:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(pos)
            self.segments.append(new_seg)

    def move(self):
        """Move each segment forward by following the segment in front of it."""
        for seg_num in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        """Turn the snake head upward unless it is currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def turn_left(self):
        """Turn the snake head left unless it is currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
      
        

    def turn_down(self):
        """Turn the snake head downward unless it is currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        

    def turn_right(self):
        """Turn the snake head right unless it is currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            

 
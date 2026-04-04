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
        self.next_heading = None


    def gen_snake(self):
        """Create the initial snake body segments at the starting positions."""
        for pos in self.starting_positions:
            self.add_segment(pos)

    def move(self):
        """Move each segment forward by following the segment in front of it."""
        # Process one queued turn per tick to prevent multiple key presses from causing an instant reverse.
        if self.next_heading is not None:
            self.head.setheading(self.next_heading)
            self.next_heading = None
        for seg_num in range(len(self.segments)- 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, pos):
        self.new_seg = Turtle("square")
        self.new_seg.color("white")
        self.new_seg.penup()
        self.new_seg.goto(pos)
        self.segments.append(self.new_seg)

    def turn_up(self):
        """Turn the snake head upward unless it is currently moving down."""
        if self.head.heading() != DOWN and self.next_heading is None:
            self.next_heading = UP

    def turn_left(self):
        """Turn the snake head left unless it is currently moving right."""
        if self.head.heading() != RIGHT and self.next_heading is None:
            self.next_heading = LEFT

    def turn_down(self):
        """Turn the snake head downward unless it is currently moving up."""
        if self.head.heading() != UP and self.next_heading is None:
            self.next_heading = DOWN

    def turn_right(self):
        """Turn the snake head right unless it is currently moving left."""
        if self.head.heading() != LEFT and self.next_heading is None:
            self.next_heading = RIGHT
            

 
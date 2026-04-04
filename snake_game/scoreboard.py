from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,260)
        
        self.score_update()

    def score_update(self):
        """Writes the score on screen"""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def level_up(self):
        """Increases the score"""
        self.score += 1
        self.score_update()
        
    def end_game(self):
        """Prints "Game Over" to the screen"""
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
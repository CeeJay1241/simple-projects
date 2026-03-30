from turtle import Turtle, Screen

paddle = Turtle(shape="square")
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.penup()
paddle.setposition(x=350,y=0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(x=paddle.xcor(), y=new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(x=paddle.xcor(), y=new_y)

screen.listen()
screen.onclick(lambda x, y: screen.bye())
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
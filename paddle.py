from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.right_paddle(coordinates)


    def right_paddle(self,location):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(location)

    def move_up(self):
        self.goto(self.xcor(),self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(),self.ycor() - 20)


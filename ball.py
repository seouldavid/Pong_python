from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_pace = 10
        self.y_pace = 10
        self.speed=0.1

    def move(self):
        self.goto(self.xcor() + self.x_pace, self.ycor() + self.y_pace)

    def bounce_top(self):
        self.y_pace *= -1

    def bounce_side(self):
        self.x_pace *= -1
        self.speed *= 0.9


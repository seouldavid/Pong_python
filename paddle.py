from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location_tup):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(location_tup)
        self.color('white')

    def pos_up(self):
        current_y = self.ycor()
        next_pos = current_y + 20
        self.goto(self.xcor(), next_pos)

    def pos_down(self):
        now_y = self.ycor()
        nxt_pos = now_y - 20
        self.goto(self.xcor(), nxt_pos)

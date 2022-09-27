from turtle import Turtle


class Board(Turtle):
    def __init__(self, location):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.location = location

    def game_over(self):
        self.goto(self.location)
        self.write(arg="Game over", move=False, align="center", font=('Arial', 18, 'bold'))

    def score_board(self, left, right):
        self.clear()
        self.goto(self.location)
        self.write(arg=f"{left} : {right}", move=False, align="center", font=('Arial', 20, 'bold'))

    def board_design(self):
        for n in range(1, 30):
            y_coord = 270 + 30 * (-1 * n)
            self.goto(0, y_coord)
            self.write(arg="|", move=False, align="center", font=('Arial', 20, 'bold'))

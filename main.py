from turtle import Screen
from paddle import Paddle
from ball import Ball
from board import Board
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('pong')
screen.tracer(0)
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
board = Board((0, 0))
score_board = Board((0, 270))
design = Board((0, 0))
design.board_design()
screen.tracer(1)

screen.listen()
screen.onkey(key='Up', fun=r_paddle.pos_up)
screen.onkey(key='Down', fun=r_paddle.pos_down)
screen.onkey(key='w', fun=l_paddle.pos_up)
screen.onkey(key='s', fun=l_paddle.pos_down)

switch = True
l_win = 0
r_win = 0
score_board.score_board(l_win, r_win)
while switch:
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_top()
    if ball.xcor() >= 360 or ball.xcor() <= -360:
        l_condition = l_paddle.ycor() + 60 >= ball.ycor() >= l_paddle.ycor() - 60
        r_condition = r_paddle.ycor() + 60 >= ball.ycor() >= r_paddle.ycor() - 60
        if l_condition and (ball.xcor() <= 0) or r_condition and (ball.xcor() >= 0):
            ball.bounce_side()

        else:
            if ball.xcor() >= 360:
                l_win += 1
            elif ball.xcor() <= -360:
                r_win += 1
            ball.x_pace *= -1
            score_board.score_board(l_win, r_win)
            # ball.move()
            # time.sleep(0.02)
            # ball.move()
            screen.tracer(0)
            ball.goto(0, 0)
            # l_paddle.goto(-380, 0)
            # r_paddle.goto(380, 0)
            time.sleep(0.5)
            screen.tracer(1)
            ball.speed = 0.1
            ball.move()

    screen.update()
    time.sleep(ball.speed)
screen.exitonclick()

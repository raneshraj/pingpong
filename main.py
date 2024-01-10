from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard
screen=Screen()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping Pong")

screen.tracer(0)

r_paddle=Paddle(((380,0))
l_paddle=Paddle((-380,0))

ball = Ball()
score=Scoreboard()
score.update_score()
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

draw=True
while draw:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>350 or ball.distance(l_paddle)<50 and ball.xcor()<-350:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.rest()
        score.lp()

    if ball.xcor()<-380:
        ball.rest()
        score.rp()



screen.exitonclick()

import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from wall import Wall
from frame import Frame
from scoreboard import Scoreboard
from scoreboard import Balls
import winsound

HELL = (1000, 1000)


def reset():
    screen = Screen()
    screen.reset()
    screen.setup(width=598, height=750)
    screen.title("  <<< Breakout Game >>>")
    screen.bgcolor("black")
    screen.tracer(15)

    wall = Wall()
    frame = Frame()
    scoreboard = Scoreboard()
    balls_left = Balls()

    def game_start():
        screen.tracer(150)
        ball = Ball()
        time.sleep(1)
        paddle = Paddle()
        screen.listen()
        winsound.Beep(1000, 100)
        screen.onkeypress(paddle.move_left, "Left")
        screen.onkeypress(paddle.move_right, "Right")
        screen.onkey(reset, "space")
        game = True
        while game:
            time.sleep(ball.SPEED)
            screen.update()
            ball.move()
            for part in paddle.paddle:
                if ball.distance(part) < 20 and ball.ycor() < -245:
                    change = ball.xcor() - paddle.center.xcor()
                    ball.paddle_hit(change)
                    winsound.Beep(8000, 80)
            for brick in wall.bricks:
                if ball.distance(brick) < 30:
                    if (brick.ycor() - 7) < ball.ycor() < (brick.ycor() + 7):
                        ball.side_hit()
                        scoreboard.score_up(brick.ycor())
                        brick.goto(HELL)
                    elif ball.ycor() < (brick.ycor() - 7):
                        ball.front_hit()
                        scoreboard.score_up(brick.ycor())
                        brick.goto(HELL)
                    elif ball.ycor() > (brick.ycor() + 7):
                        ball.brick_top_hit()
                        scoreboard.score_up(brick.ycor())
                        brick.goto(HELL)
                    winsound.Beep(13000, 50)
            if ball.ycor() > 365:
                ball.front_hit()
            if 292 > ball.xcor() >= 285 or -297 < ball.xcor() <= -290:
                ball.side_hit()
            if ball.ycor() < -400 or ball.xcor() < -310 or ball.xcor() > 310:
                if not balls_left.balls_down():
                    return
                paddle.paddle_reset()
                game = False
        game_start()
    game_start()
    screen.exitonclick()


reset()

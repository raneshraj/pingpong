from turtle import Turtle

PADDLE_SIZE = 63
PADDLE_SPEED = 17
X = -(PADDLE_SIZE/2)
HELL = (666, 666)
positions = []

for z in range(PADDLE_SIZE):
    pos = (X,-250)
    X += 1
    positions.append(pos)


class Paddle:
    def __init__(self):
        self.paddle = []
        self.create_paddle()
        self.center = self.paddle[PADDLE_SIZE//2]

    def create_paddle(self):
        for position in positions:
            part = Turtle()
            part.shape("square")
            part.shapesize(0.2, 0.02)
            part.color("grey")
            part.penup()
            part.goto(position)
            self.paddle.append(part)

    def move_left(self):
        if self.paddle[0].xcor() > -287:
            for part in self.paddle:
                part.goto(part.xcor() - PADDLE_SPEED, part.ycor())

    def move_right(self):
        if self.paddle[len(self.paddle)-1].xcor() < 280:
            for part in self.paddle:
                part.goto(part.xcor() + PADDLE_SPEED, part.ycor())

    def paddle_reset(self):
        for part in self.paddle:
            part.goto(HELL)
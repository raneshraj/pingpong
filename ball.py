import random
from turtle import Turtle

COLOR = "pink"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(COLOR)
        self.shapesize(0.5, 0.5)
        self.penup()
        self.setheading(270)
        self.SPEED = 0.015

    def move(self):
        self.forward(7)

    def side_hit(self):
        if 90 < self.heading() < 270:
            self.setheading((270 - self.heading()) + 270)
        elif 270 < self.heading() < 359:
            self.setheading(270 - (self.heading() - 270))
        elif 0 < self.heading() < 90:
            self.setheading((90 - self.heading()) + 90)
        elif 90 < self.heading() < 180:
            self.setheading(90 - (self.heading() - 90))

    def paddle_hit(self, change):
        self.setheading(90 - change * 1.75)
        self.forward(5)
        if self.SPEED > 0.008:
            self.SPEED -= 0.001

    def front_hit(self):
        if 0 < self.heading() < 90:
            self.setheading(90 - self.heading() + 270)
        elif self.heading() == 90:
            self.setheading(random.choice((88, 92)))
        elif 90 < self.heading() < 180:
            self.setheading(270 - (self.heading() - 90))

    def brick_top_hit(self):
        if 270 < self.heading() < 359:
            self.setheading(90 - (self.heading() - 270))
        elif 180 < self.heading() < 270:
            self.setheading(90 + (270 - self.heading()))
from turtle import Turtle


class Frame:
    def __init__(self):
        top = Turtle('square')
        top.penup()
        top.shapesize(0.5, 299)
        top.color('light grey')
        top.goto(0, 375)

        left_wall = Turtle('square')
        left_wall.penup()
        left_wall.shapesize(750, 0.5)
        left_wall.color('light grey')
        left_wall.goto(-300, 0)

        right_wall = Turtle('square')
        right_wall.penup()
        right_wall.shapesize(750, 0.5)
        right_wall.color('light grey')
        right_wall.goto(293, 0)
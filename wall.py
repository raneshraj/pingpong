from turtle import Turtle

colors = ["yellow", "green", "orange", "red"]


class Wall:
    def __init__(self):
        self.bricks = []
        self.create_wall()

    def create_wall(self):
        x_pos = -278
        y_pos = 140
        for color in colors:
            for y in range(0, 2):
                for x in range(0, 14):
                    new_brick = Turtle("square")
                    new_brick.shapesize(0.6, 2)
                    new_brick.color(color)
                    new_brick.penup()
                    new_brick.goto(x_pos, y_pos)
                    self.bricks.append(new_brick)
                    x_pos += 42
                x_pos = -278
                y_pos += 15



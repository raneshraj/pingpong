from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_s = 0
        self.right_s = 0


    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_s, align="center", font=("digital", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_s, align="center", font=("digital", 80, "normal"))

    def lp(self):
        self.left_s += 1
        self.update_score()

    def rp(self):
        self.right_s += 1
        self.update_score()

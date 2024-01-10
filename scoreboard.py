from turtle import Turtle
FONT = ("courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.print_score()

    def score_up(self, brick):
        if brick == 140 or brick == 155:
            self.score += 1
            self.print_score()
        elif brick == 170 or brick == 185:
            self.score += 3
            self.print_score()
        elif brick == 200 or brick == 215:
            self.score += 5
            self.print_score()
        elif brick == 230 or brick == 245:
            self.score += 7
            self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-150, 300)
        self.write(f"Score: {self.score}", align="center", font=FONT)


class Balls(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.balls = 3
        self.print_balls()

    def print_balls(self):
        self.clear()
        self.goto(150, 300)
        self.write(f"Balls: {self.balls}", align="center", font=FONT)

    def balls_down(self):
        if self.balls > 0:
            self.balls -= 1
            self.print_balls()
            return True
        else:
            self.print_balls()
            self.print_over()
            return False

    def print_over(self):
        self.clear()
        self.goto(0, 330)
        self.write("<<< GAME OVER >>>", align="center", font=FONT)
        self.goto(0, 0)
        self.write("Press SPACE to restart", align="center", font=("courier", 13, "normal"))
